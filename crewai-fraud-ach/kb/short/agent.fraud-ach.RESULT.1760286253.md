```json
{
  "id": "02871be14415d840",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286253,
  "host_pid": "9e6742732c60:1",
  "hash": "2089b722a8aa0f00d62fb5dd0670b401c2a9b27a495552e2fb7b930c7a11a62d",
  "cid": "QmV12089b722a8aa0f00d62fb5dd0670b401c2a9b27a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286253,
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
      "evaluated_at": 1760286253
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
  "sig": "575ab43060cd4202a6381d883e71820b87b901461ceed0602d05fe3885562d26"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467798287
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285765, 'matching_hash': 'b1c6e5e3cdd02671'}}}