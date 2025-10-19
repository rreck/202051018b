```json
{
  "id": "7a9534bed81733f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287319,
  "host_pid": "9e6742732c60:1",
  "hash": "0389aef41c92c50befcddf7e944edcb5a72a71d58b50cc142e3670625a29144d",
  "cid": "QmV10389aef41c92c50befcddf7e944edcb5a72a71d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287319,
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
      "evaluated_at": 1760287319
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
  "sig": "5df348c2feeefc03e6d170169059f5a999d257f249819871570a153a90115cb0"
}
```

Fraud detected: duplicate_transaction (score: 73)
Transaction: 021000024088542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 62, 'details': {'transaction_count': 56, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285763, 'matching_hash': '45759aa393537ed9'}}}een': 1760285763, 'matching_hash': 'b2544ae352aa282b'}}}