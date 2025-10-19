```json
{
  "id": "c9ad084713d93f60",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286039,
  "host_pid": "9e6742732c60:1",
  "hash": "841633dcc2cf7333c82441403653576b425c311ca1b9ec79958077e7e1967822",
  "cid": "QmV1841633dcc2cf7333c82441403653576b425c311c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286039,
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
      "evaluated_at": 1760286039
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
  "sig": "a71bd9c63fe846c272fdba0fcf5a8f63313ee758f844a500c3a7fd63b30ae04f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100272414433
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285764, 'matching_hash': 'f489e4bd64364941'}}}