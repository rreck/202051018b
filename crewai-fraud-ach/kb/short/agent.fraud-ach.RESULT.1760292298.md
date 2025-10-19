```json
{
  "id": "1c564dddc72eda7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292298,
  "host_pid": "9e6742732c60:1",
  "hash": "6999b185247b78a6cebceeaddfe0a67cc37c647f12f30e8bbc61eefdd0cb7da8",
  "cid": "QmV16999b185247b78a6cebceeaddfe0a67cc37c647f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292298,
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
      "evaluated_at": 1760292298
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
  "sig": "2daf3b9ce989459a73d2e58f2232e363a0c65990850763ff6bc4d8526465f4a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270650471
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285765, 'matching_hash': '471e898b7e147a60'}}}