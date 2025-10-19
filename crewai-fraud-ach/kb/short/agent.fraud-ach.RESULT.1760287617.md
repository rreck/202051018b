```json
{
  "id": "fc46809c3179acfb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287617,
  "host_pid": "9e6742732c60:1",
  "hash": "82d44277479b81264e01b4d347d632e4b738a1cb2999a6d696a79ffecad03aad",
  "cid": "QmV182d44277479b81264e01b4d347d632e4b738a1cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287617,
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
      "evaluated_at": 1760287617
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
  "sig": "5d574dc4e0b0c7ead34029c7afd67a154bc9fa5aca427c0d745acf418c984eca"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 021000022135017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285765, 'matching_hash': 'ca41710ea386559e'}}}