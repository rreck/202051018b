```json
{
  "id": "546b178ed37a7519",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286425,
  "host_pid": "9e6742732c60:1",
  "hash": "22997c73519ee62430a2f82b62a85be93dd847f27865ac15934fc67b64c860b2",
  "cid": "QmV122997c73519ee62430a2f82b62a85be93dd847f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286425,
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
      "evaluated_at": 1760286425
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
  "sig": "8f5a675627af52c5d1b91a1f79f59be32d5622f38db5097633aa4ac22a621c8c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249225817
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': 'b4dc0a1cb279f16e'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': '1ddc8562b5a9ecf0'}}}