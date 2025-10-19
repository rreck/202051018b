```json
{
  "id": "a07b7c4568a414bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285868,
  "host_pid": "9e6742732c60:1",
  "hash": "89791dfa51dedfa8b38ffd86690749ea8fa429b5c76e7cd6167a1a17aba2e0a5",
  "cid": "QmV189791dfa51dedfa8b38ffd86690749ea8fa429b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285868,
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
      "evaluated_at": 1760285868
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
  "sig": "58beb2f43be4f12475a96e78f2fc6f393ff35e9db412cdfbc12caaf57c42a548"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000036013549
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285763, 'matching_hash': 'f1471db42dbf1c81'}}}