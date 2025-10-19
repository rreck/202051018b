```json
{
  "id": "bc5b2318fa19a019",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286371,
  "host_pid": "9e6742732c60:1",
  "hash": "e9727c250e0652803e3f9aad14e51cbb80eeed69596a8785638d65825bbf4197",
  "cid": "QmV1e9727c250e0652803e3f9aad14e51cbb80eeed69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286371,
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
      "evaluated_at": 1760286371
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
  "sig": "fac545e79806b3be64826df67696e695c7e356f46c387597c7a6a7a0b1b3c3be"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000023479394
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '601e7e272d8441f2'}}}