```json
{
  "id": "bff32e5bfbe57658",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289402,
  "host_pid": "9e6742732c60:1",
  "hash": "57d8fe01f6024a97714cb64d41039e497de202e93e7c5d42be09f8cd4f4f02ac",
  "cid": "QmV157d8fe01f6024a97714cb64d41039e497de202e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289402,
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
      "evaluated_at": 1760289402
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
  "sig": "03b27cbc30658f02eb3e34024b8e306af5c928c3cb52e3c51b67a7852441f8a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245537248
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 17835790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285765, 'matching_hash': '5bdcebee79eae34d'}}}