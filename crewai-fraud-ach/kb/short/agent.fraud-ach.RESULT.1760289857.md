```json
{
  "id": "61177443a6631423",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289857,
  "host_pid": "9e6742732c60:1",
  "hash": "96b5b7d7bd8b93095d2029b053976485cdee073ca8da2c2b31c36fd36504b4e6",
  "cid": "QmV196b5b7d7bd8b93095d2029b053976485cdee073c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289857,
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
      "evaluated_at": 1760289857
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
  "sig": "4dd0ec798e285768e6d1a24625af3e5cc2130ca1414247d2cfb24efb931931d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026044300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 51882255, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': '19d391c08a2c00ab'}}}