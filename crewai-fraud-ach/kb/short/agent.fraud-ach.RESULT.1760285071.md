```json
{
  "id": "103fd5436349f009",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285071,
  "host_pid": "9e6742732c60:1",
  "hash": "872d4e3839785102dfb6d975f592427b3f7b643fa211c1b8406f4d5d2f5c7c43",
  "cid": "QmV1872d4e3839785102dfb6d975f592427b3f7b643f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285071,
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
      "evaluated_at": 1760285071
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
  "sig": "f9dd0b5d9419da52708c5f002960a80525423bec074022a6633b15820bb8cf8a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}