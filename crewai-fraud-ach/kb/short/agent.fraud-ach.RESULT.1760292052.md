```json
{
  "id": "0736e4d24afc634b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292052,
  "host_pid": "9e6742732c60:1",
  "hash": "71f8c7e6b0b80adfc788141712ca413a823b8caf9a647f93c2dc605a36bb9dd0",
  "cid": "QmV171f8c7e6b0b80adfc788141712ca413a823b8caf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292052,
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
      "evaluated_at": 1760292052
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
  "sig": "2165bfe752f92226f2314868ef41b0c423d26e842be1473b5b25895e762124b9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155063461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 59544072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285764, 'matching_hash': '55217e698cd3f78f'}}}