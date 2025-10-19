```json
{
  "id": "fb54b2249f35fb93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286225,
  "host_pid": "9e6742732c60:1",
  "hash": "1863ae82950ef81d42e7b5caf836747384cd859b45394bd4f1be1b7c9cb55d95",
  "cid": "QmV11863ae82950ef81d42e7b5caf836747384cd859b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286225,
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
      "evaluated_at": 1760286225
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
  "sig": "b8768990b6aee3de0ce7efa9d123b7a9b475c182ee71a840d176b8695754747b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270650471
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': '471e898b7e147a60'}}}