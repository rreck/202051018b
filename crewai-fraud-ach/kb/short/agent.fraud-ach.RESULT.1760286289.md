```json
{
  "id": "98aeceb1bab2c39c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286289,
  "host_pid": "9e6742732c60:1",
  "hash": "291c80317e9c4fbbec5da8c8c3016cf3bc6d7bb4ffe5fac1bacea560437de091",
  "cid": "QmV1291c80317e9c4fbbec5da8c8c3016cf3bc6d7bb4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286289,
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
      "evaluated_at": 1760286289
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
  "sig": "2ffa7aed4d9fb008c9047045b4106f9eeb20ebea7e149956bbc9e1170fcbf3ea"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}