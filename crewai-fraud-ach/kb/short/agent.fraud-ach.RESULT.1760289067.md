```json
{
  "id": "3e75e6d4d4e76f6f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289067,
  "host_pid": "9e6742732c60:1",
  "hash": "516e36de9d3d9193a78a1f7c2356ad90127a3b4ffb9de8ca387bc9e4b850990f",
  "cid": "QmV1516e36de9d3d9193a78a1f7c2356ad90127a3b4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289067,
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
      "evaluated_at": 1760289067
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
  "sig": "ba979c90a38f82a06ea812d34795fdb6500126254ba34e2b4c63b98e72d14744"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 026009597287610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 112000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285765, 'matching_hash': 'd127b5f232f25796'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}