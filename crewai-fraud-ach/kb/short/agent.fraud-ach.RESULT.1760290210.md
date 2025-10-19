```json
{
  "id": "636ff4e2047752b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290210,
  "host_pid": "9e6742732c60:1",
  "hash": "5f25b922da7e6ed50dc6622cc08f3c86cbee7c838c809000828bb687e4f7f46a",
  "cid": "QmV15f25b922da7e6ed50dc6622cc08f3c86cbee7c83",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290210,
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
      "evaluated_at": 1760290210
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
  "sig": "eb9ef845217e3b43e44ca698a393a0466ac5c7447837fffa7b6e56c50e63c950"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025325708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 46404432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285765, 'matching_hash': '23dd43a9dda0a05d'}}}