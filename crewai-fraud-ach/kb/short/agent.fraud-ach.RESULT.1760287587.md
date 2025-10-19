```json
{
  "id": "bc31121e2254458c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287587,
  "host_pid": "9e6742732c60:1",
  "hash": "8e4e29316337f88d34b7474f39d0b38dfea7b8ebc65680e3a1086027fddbe83f",
  "cid": "QmV18e4e29316337f88d34b7474f39d0b38dfea7b8eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287587,
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
      "evaluated_at": 1760287587
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
  "sig": "b4ae80a967346effe38d18caa46aedacbb705e51a94ad926d57de4cca3c980b6"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 026009597800882
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 13351455, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285765, 'matching_hash': 'e972b74e8fc22124'}}}