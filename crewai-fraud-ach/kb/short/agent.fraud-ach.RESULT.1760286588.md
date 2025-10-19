```json
{
  "id": "f03df70cf32832b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286588,
  "host_pid": "9e6742732c60:1",
  "hash": "ba79c010d0119c6f8c1080b3c8b82871a7b40dc7bf4fbaf32c0514218b9f6664",
  "cid": "QmV1ba79c010d0119c6f8c1080b3c8b82871a7b40dc7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286588,
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
      "evaluated_at": 1760286588
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
  "sig": "fdd67e429a7700302c50b9a9cae704487de1f2f0d3b6eaf0bf3596cdc09d204e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029964192
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}