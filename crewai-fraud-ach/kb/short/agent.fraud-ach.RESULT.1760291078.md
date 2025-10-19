```json
{
  "id": "3bd51fd5b43dfca8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291078,
  "host_pid": "9e6742732c60:1",
  "hash": "b41bfa82cda12fae4463780a07bf995819e4afe1105c03760646cb1e5ac93afc",
  "cid": "QmV1b41bfa82cda12fae4463780a07bf995819e4afe1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291078,
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
      "evaluated_at": 1760291078
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
  "sig": "3f54b1395d677eff672f3afe2f3cf9253a7a8a5225fcdd7d561c6eb504137370"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463882943
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 20585328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}