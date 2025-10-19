```json
{
  "id": "b3e026b41fb18f88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291393,
  "host_pid": "9e6742732c60:1",
  "hash": "f4c2daddcba68cc88a7d83f8dce390c4ef1b91a8bac12334ba3939480d99346f",
  "cid": "QmV1f4c2daddcba68cc88a7d83f8dce390c4ef1b91a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291393,
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
      "evaluated_at": 1760291393
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "d9be2de011d3e9cb2693465a59e6fc5277d857b7a3cf02efb37608313ef643e5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028270724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': 'c4ee7f0f971d402b'}}} 1760285763, 'matching_hash': '3e77f188c48013ab'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}