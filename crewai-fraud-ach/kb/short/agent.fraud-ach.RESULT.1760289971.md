```json
{
  "id": "898f82cc26c7b0d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289971,
  "host_pid": "9e6742732c60:1",
  "hash": "d4bc15f805a0c72b19392a454431f477083258ce4ae6f1701c96415e257751f9",
  "cid": "QmV1d4bc15f805a0c72b19392a454431f477083258ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289971,
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
      "evaluated_at": 1760289971
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
  "sig": "cc5bff3bccc78c0f3b6ad2c32ebeb44ee8d728d042c8d1f6303f7573ed6d8993"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023973780
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 12110880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': 'a6cf7acef53d66c2'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018325}}}