```json
{
  "id": "cf2accb009709ba0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285976,
  "host_pid": "9e6742732c60:1",
  "hash": "a94ccdadc3360f25e2750c7bd6daf965a4e7cda0533126426079775491a9d697",
  "cid": "QmV1a94ccdadc3360f25e2750c7bd6daf965a4e7cda0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285976,
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
      "evaluated_at": 1760285976
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
  "sig": "9db5d1f2d8a83bd52be74e858d17cde178f85148685faa76a5543885e7cf5339"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029163318
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285765, 'matching_hash': 'b5567c8565e47211'}}}