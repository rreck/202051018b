```json
{
  "id": "17d7be9f0348b946",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286254,
  "host_pid": "9e6742732c60:1",
  "hash": "3f6847959bf5323a733ac10b1cbed1e6875324a3a84eb8dbceaf17bbfcfad987",
  "cid": "QmV13f6847959bf5323a733ac10b1cbed1e6875324a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286254,
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
      "evaluated_at": 1760286254
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
  "sig": "7b1e975bf8c3822c4bbf5ca8573bada1fc294c74030590eb245a26512fb06e6e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000246259253
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285765, 'matching_hash': '5582c4cd79a5b751'}}}