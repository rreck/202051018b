```json
{
  "id": "af22d228f49f6e14",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286820,
  "host_pid": "9e6742732c60:1",
  "hash": "ab4ac98f148416de1bcadabde4cd07dc76b676aa4878da02d2ef1479cb469863",
  "cid": "QmV1ab4ac98f148416de1bcadabde4cd07dc76b676aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286820,
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
      "evaluated_at": 1760286820
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
  "sig": "d184b4d94ac6e627fe2c4bcd2f9d247009f9a05f87439fe82d0981abf1020dc7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000248914863
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}