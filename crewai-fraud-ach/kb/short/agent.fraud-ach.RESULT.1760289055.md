```json
{
  "id": "43914369c357f02f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289055,
  "host_pid": "9e6742732c60:1",
  "hash": "d724fc56cfc1a697cecef4172f3e44c054d33702fb7a6853b2b9327f4a8a2a01",
  "cid": "QmV1d724fc56cfc1a697cecef4172f3e44c054d33702",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289055,
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
      "evaluated_at": 1760289055
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
  "sig": "46998cf76522bf44ce750be876d44558884fb7884ce153090e019163ab54d1d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591169500
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 22264816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '9cbc2ba8ece9eaee'}}}