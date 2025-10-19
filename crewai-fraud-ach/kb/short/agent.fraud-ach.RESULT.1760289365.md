```json
{
  "id": "59896f89ead7bfd0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289365,
  "host_pid": "9e6742732c60:1",
  "hash": "4c50df5f9c73f361a4bc32f4e0b4c72a2da8a3830efcbff664202cad6febb207",
  "cid": "QmV14c50df5f9c73f361a4bc32f4e0b4c72a2da8a383",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289365,
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
      "evaluated_at": 1760289365
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
  "sig": "d2120b0e83aec7ac4e0bdfdea788b99c2dffd516e5e5183dc3c097f9d7e01280"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594081907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 59962034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': 'b8f6a044d6b1da81'}}}aly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 4.0, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7743228}}}