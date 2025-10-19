```json
{
  "id": "a322e28b1be5fa70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291165,
  "host_pid": "9e6742732c60:1",
  "hash": "8bac18fa5d681632a3cfd5bb11cf663b6a38690b37b995c0841f426ac6ecda98",
  "cid": "QmV18bac18fa5d681632a3cfd5bb11cf663b6a38690b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291165,
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
      "evaluated_at": 1760291165
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
  "sig": "1acab2c83ee78bac85da82466ebacda0dcc9fc75bffdff61316dadf47ebc9d8e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158656793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 50919792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285765, 'matching_hash': 'b1ac6f9d66d66d2b'}}}