```json
{
  "id": "fdb7de3baaf74b7c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287135,
  "host_pid": "9e6742732c60:1",
  "hash": "e0104dff21000459efe917ddd2b6d3ddb04adfe667cb533da94a6e554fbb9418",
  "cid": "QmV1e0104dff21000459efe917ddd2b6d3ddb04adfe6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287135,
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
      "evaluated_at": 1760287135
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
  "sig": "ced6da3ad488181eddfffc4ec82d3361eaf24d87d7de597e1f048d7716303bc4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242007664
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285765, 'matching_hash': 'b61887453511199f'}}}