```json
{
  "id": "ae76f5622083db44",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286523,
  "host_pid": "9e6742732c60:1",
  "hash": "c1800dcc97c24777e57de2018d4c127634a688af7f5a71fa52405c18a4db4837",
  "cid": "QmV1c1800dcc97c24777e57de2018d4c127634a688af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286523,
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
      "evaluated_at": 1760286523
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
  "sig": "3e42071660bd07eda55d2510c8bb10f5ef1245ce380b4203f61c43c96317e91e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029384681
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285764, 'matching_hash': '45a3ccbce684d395'}}}