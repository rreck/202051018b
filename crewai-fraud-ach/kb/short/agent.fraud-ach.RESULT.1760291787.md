```json
{
  "id": "854bfa51aec9de00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291787,
  "host_pid": "9e6742732c60:1",
  "hash": "affb40df7fe19410e44c7e97c5f4d17f458a3d4a4a18984f4f860b6762afefad",
  "cid": "QmV1affb40df7fe19410e44c7e97c5f4d17f458a3d4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291787,
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
      "evaluated_at": 1760291787
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
  "sig": "f9f18ca103770b612f606b47bcc553916d4140eb15db0789f04e2f221eee0d14"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271528987
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 74483745, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': '52a7e62e45a672d0'}}}