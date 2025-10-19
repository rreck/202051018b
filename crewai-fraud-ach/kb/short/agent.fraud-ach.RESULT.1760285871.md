```json
{
  "id": "cc9bf17469eb76a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285871,
  "host_pid": "9e6742732c60:1",
  "hash": "8816adf853179172ae0361dde147428c95c89030e611ccba96a151e3226f0f02",
  "cid": "QmV18816adf853179172ae0361dde147428c95c89030",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285871,
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
      "evaluated_at": 1760285871
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
  "sig": "c83bf241694eb9e37046321165274ea50b15944fc2ae2ce10b931d40ce6479c7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000034624068
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285763, 'matching_hash': 'e9c21d379839efb6'}}}