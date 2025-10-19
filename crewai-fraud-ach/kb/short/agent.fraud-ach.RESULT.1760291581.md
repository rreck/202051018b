```json
{
  "id": "0d2803ea8e61eb8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291581,
  "host_pid": "9e6742732c60:1",
  "hash": "4b749f0e49e56cc695ef46c9f23c5c336a296b2045d5dd30add89ea186e95692",
  "cid": "QmV14b749f0e49e56cc695ef46c9f23c5c336a296b20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291581,
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
      "evaluated_at": 1760291581
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
  "sig": "de4082ce983f88d265aa8b5b2c1604c7bf0b389e2ffaae7d55932d45be268ade"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245381675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 29195738, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': 'fa6674ee96d393a2'}}}