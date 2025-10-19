```json
{
  "id": "58422f674ecfb746",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286336,
  "host_pid": "9e6742732c60:1",
  "hash": "8c60a4a48f12189403c629e20618f41c766a9bf25d4fa53fe3293e695f68cef0",
  "cid": "QmV18c60a4a48f12189403c629e20618f41c766a9bf2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286336,
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
      "evaluated_at": 1760286336
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
  "sig": "fe1df3d9cc21d08cd6aea63a094206f7d4791acb1158c7efdc760e7a7cb34097"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000025341279
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': 'e2ff1695635a899d'}}}