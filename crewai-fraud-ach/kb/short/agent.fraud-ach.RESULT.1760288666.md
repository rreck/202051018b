```json
{
  "id": "5d044523a251f5f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288666,
  "host_pid": "9e6742732c60:1",
  "hash": "90fb2c065f84a3c3c6c8aa6ed21b5a5470ac657e4d1d8f1a42835fe1cd069be5",
  "cid": "QmV190fb2c065f84a3c3c6c8aa6ed21b5a5470ac657e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288666,
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
      "evaluated_at": 1760288666
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
  "sig": "3a59bb35e91a16fc12d85700357e05fe6bcd8bfea222d1a5c551ad4041046fe2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032369849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 41747600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285764, 'matching_hash': '11b86d7f8733bf3d'}}}