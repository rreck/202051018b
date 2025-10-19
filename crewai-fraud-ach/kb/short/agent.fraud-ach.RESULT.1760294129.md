```json
{
  "id": "8496d2d3cbdd8c35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294129,
  "host_pid": "9e6742732c60:1",
  "hash": "93898b0eca916e188451bff97758e24642ba2f6d17613279564e1c66d0d62a7e",
  "cid": "QmV193898b0eca916e188451bff97758e24642ba2f6d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294129,
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
      "evaluated_at": 1760294129
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
  "sig": "5739d84e0d6a793e54f3a6dc513036b16aa8958fe519c89088b71d2b612c9319"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023944450
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 17649400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '3c29e184ba733f5e'}}}