```json
{
  "id": "fe86f0d198cab395",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294518,
  "host_pid": "9e6742732c60:1",
  "hash": "16f26d06797b1cd07f933b711980896e39ef25b60cf8e76cc2d93439d0fb3140",
  "cid": "QmV116f26d06797b1cd07f933b711980896e39ef25b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294518,
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
      "evaluated_at": 1760294518
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
  "sig": "54066593df15f36f727d371bca6a42c55780e4d8b397c4fd3a34f8c37120a6bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029236644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 54443005, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': 'c69cf0de1758a1d7'}}}