```json
{
  "id": "5649d7664a75468f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288686,
  "host_pid": "9e6742732c60:1",
  "hash": "570573d73f29a829be37862765a0c5d3bc21ee0e59abec6cb7e8f8bdee34a344",
  "cid": "QmV1570573d73f29a829be37862765a0c5d3bc21ee0e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288686,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760288686
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "b0f88a884fe71c3e98d3e7cc5c5b114be21d52eb1bedc4fc8a890d295aeac5a0"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 026009594828050
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 101000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': '3e77f188c48013ab'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}