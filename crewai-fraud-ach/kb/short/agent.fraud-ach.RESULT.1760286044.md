```json
{
  "id": "6e9cdf1ba9f73d5b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286044,
  "host_pid": "9e6742732c60:1",
  "hash": "e75f0ff0585ed3041c95da7a13a6d09ea9d171dc83bf138bef047241f0bec5ac",
  "cid": "QmV1e75f0ff0585ed3041c95da7a13a6d09ea9d171dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286044,
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
      "evaluated_at": 1760286044
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
  "sig": "e22638d385c8850525fd92326056e869933c2dc778298298fb6a3f19e3629d42"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469007601
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285765, 'matching_hash': '9208fda71b3c290c'}}}