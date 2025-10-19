```json
{
  "id": "a8cb03f6e9cda872",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293772,
  "host_pid": "9e6742732c60:1",
  "hash": "8db566eacfb14f9629453531ed4b4a5adfcd780645e055a1ad5f00b3aa1fe391",
  "cid": "QmV18db566eacfb14f9629453531ed4b4a5adfcd7806",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293772,
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
      "evaluated_at": 1760293772
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
  "sig": "5b904ed424ad1d5ba39b082d93fd055002beca1d9b81e2b4d7827f29e9e5b981"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243367348
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 73081800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': 'a37b6eb1b4e3b31b'}}}