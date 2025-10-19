```json
{
  "id": "73d8612a9931e146",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286837,
  "host_pid": "9e6742732c60:1",
  "hash": "60907a2874a049815bfa9024add30dd3076b0688791aa0e9baac12f3944030fa",
  "cid": "QmV160907a2874a049815bfa9024add30dd3076b0688",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286837,
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
      "evaluated_at": 1760286837
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
  "sig": "17be95701dddb7f7039bd374de64319dc2f3aa3c77708452183c0e0e059aa014"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100277559927
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '07b51054ae5371fb'}}}