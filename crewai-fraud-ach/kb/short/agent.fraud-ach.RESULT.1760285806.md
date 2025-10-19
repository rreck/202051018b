```json
{
  "id": "f9865a7d9492fc53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285806,
  "host_pid": "9e6742732c60:1",
  "hash": "603cdd3ca61fd82b309eedd7b9ac6441bc046cd150ac1e953124e170435bdbd8",
  "cid": "QmV1603cdd3ca61fd82b309eedd7b9ac6441bc046cd1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285806,
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
      "evaluated_at": 1760285806
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
  "sig": "d195ba0d876174605edbf4032c95770d1f8597fa1a09584d54238c1c6b58acac"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009593702879
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285763, 'matching_hash': '1b01d510f5fcfc0c'}}}