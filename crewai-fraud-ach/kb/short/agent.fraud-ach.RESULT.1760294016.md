```json
{
  "id": "0881bd2b0f27e20d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294016,
  "host_pid": "9e6742732c60:1",
  "hash": "8c584d185f927f85055595d1495f80cda75a03578a09683941e22255ca46180e",
  "cid": "QmV18c584d185f927f85055595d1495f80cda75a0357",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294016,
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
      "evaluated_at": 1760294016
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
  "sig": "d37c01e27f95452e4ed58c59b5c64c2011a86ba1fbbbf078113707c68012db9a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026797438
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 85839450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285764, 'matching_hash': '15a6693010fc8a85'}}}