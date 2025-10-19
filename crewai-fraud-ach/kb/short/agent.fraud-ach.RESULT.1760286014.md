```json
{
  "id": "35874e4fd0022f46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286014,
  "host_pid": "9e6742732c60:1",
  "hash": "92f74bda568357e734157eafdaa7e4518209c544af4becb2814cf9fb09a2e766",
  "cid": "QmV192f74bda568357e734157eafdaa7e4518209c544",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286014,
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
      "evaluated_at": 1760286014
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
  "sig": "47ea6776b2fbd4a7a155c3c1dbd34d75cff05330411fe97be76259dd68283ffa"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000021513577
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285765, 'matching_hash': '2d9e7d16ad0b5ba4'}}}