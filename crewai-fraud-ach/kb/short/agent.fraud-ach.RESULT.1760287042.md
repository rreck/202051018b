```json
{
  "id": "3ebd3ea2d78e9761",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287042,
  "host_pid": "9e6742732c60:1",
  "hash": "9aa08abeb02071f9b3184324d6a29a523d456a928574b9860afce271973016d1",
  "cid": "QmV19aa08abeb02071f9b3184324d6a29a523d456a92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287042,
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
      "evaluated_at": 1760287042
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
  "sig": "01ae9b63dda33487ff4bc98fa613463f6df9b354849b645d206a3c099f5ce046"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000020633236
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285763, 'matching_hash': 'c43a110d8b947858'}}}