```json
{
  "id": "bbece04c3b7c62d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291689,
  "host_pid": "9e6742732c60:1",
  "hash": "ed36160eea7c7649a4989b1f5dd42f143dd6205c43fa9988c7105e2660783f6c",
  "cid": "QmV1ed36160eea7c7649a4989b1f5dd42f143dd6205c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291689,
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
      "evaluated_at": 1760291689
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
  "sig": "2aacf2d0b6eb9108537d6547c9f6d5a722eaf414b62aa8074c13c333f400569c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462098783
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 37223374, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '4ea38d6416e4381e'}}}maly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.78, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7365830}}}