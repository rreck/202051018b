```json
{
  "id": "42ae97470d1dce8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285910,
  "host_pid": "9e6742732c60:1",
  "hash": "53b9c79813dafed0fb93484677b595944acdd93a07a06096384996df1d36ec03",
  "cid": "QmV153b9c79813dafed0fb93484677b595944acdd93a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285910,
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
      "evaluated_at": 1760285910
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
  "sig": "72875d0205a77d63d6ba856abefa51a7de69f355005fbb62dddaf2ed553d452d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000024544859
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285763, 'matching_hash': '21e0fdbcd06f2d49'}}}