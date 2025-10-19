```json
{
  "id": "8bbdb4b7da3df67c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291352,
  "host_pid": "9e6742732c60:1",
  "hash": "219e5728981c61a87ba6e28aa645ce9d6411e9df2ba1558195e7e5685d483be1",
  "cid": "QmV1219e5728981c61a87ba6e28aa645ce9d6411e9df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291352,
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
      "evaluated_at": 1760291352
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
  "sig": "3b26e64dbc537a3e03e0cee7253774981b3f0b4a8b0066d59781de8ec5e3e3a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242172457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 81512410, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': '180325de6151a8c9'}}}