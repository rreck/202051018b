```json
{
  "id": "d21066c803fd0afb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285968,
  "host_pid": "9e6742732c60:1",
  "hash": "cff871c858e70ed9266c13d7e13137e5bd925fcf6de6d46ac299e011ee48602a",
  "cid": "QmV1cff871c858e70ed9266c13d7e13137e5bd925fcf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285968,
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
      "evaluated_at": 1760285968
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
  "sig": "414724d6c68dde18d101325ccdc840835477442d5063f7916ce4a4301eab7690"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469776996
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285763, 'matching_hash': '22919e1176d7109e'}}}