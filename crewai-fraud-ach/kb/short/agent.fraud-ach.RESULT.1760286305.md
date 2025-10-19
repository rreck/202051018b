```json
{
  "id": "abe6c9c7c8d95dc6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286305,
  "host_pid": "9e6742732c60:1",
  "hash": "fd3180e94ec403ef75241da6c6fb4c7ff9e6cc9b57cd3a9a85c423404acb4148",
  "cid": "QmV1fd3180e94ec403ef75241da6c6fb4c7ff9e6cc9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286305,
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
      "evaluated_at": 1760286305
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
  "sig": "f410dd2666e1f6b5f8ca1453b75bccd4a9a3e3b44da8990ba7301ff17d5fc637"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029233033
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285763, 'matching_hash': 'f6bf3c76ea3935d9'}}}