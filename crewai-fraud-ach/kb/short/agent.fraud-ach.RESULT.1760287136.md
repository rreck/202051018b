```json
{
  "id": "2226c84ab4085c28",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287136,
  "host_pid": "9e6742732c60:1",
  "hash": "7611f4560ef5c6236f181f6c339e7267f97af7a508510c1c2339951ac15f4486",
  "cid": "QmV17611f4560ef5c6236f181f6c339e7267f97af7a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287136,
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
      "evaluated_at": 1760287136
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "a300356caec0526c261b7d7b7352a01bc165a5badacda9644a227b1524955022"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105155194168
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17916605, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285765, 'matching_hash': '7ab74b64ae25594e'}}}