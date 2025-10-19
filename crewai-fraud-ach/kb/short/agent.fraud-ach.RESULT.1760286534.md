```json
{
  "id": "a9e22ae891441dc4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286534,
  "host_pid": "9e6742732c60:1",
  "hash": "c06918c3ae764adc9dacb6e4b4bda01711dca79307b51348857d94973aaad6a4",
  "cid": "QmV1c06918c3ae764adc9dacb6e4b4bda01711dca793",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286534,
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
      "evaluated_at": 1760286534
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
  "sig": "2036fc8ec1e621c808ce4de318d63ff121075a253899d5eaa6b7de1169e116fc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201466702370
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285765, 'matching_hash': 'c2e86be7e57e9a06'}}}