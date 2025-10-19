```json
{
  "id": "f799224d42e8b6b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286045,
  "host_pid": "9e6742732c60:1",
  "hash": "541150c08c730db4c27d5406977506c71774d025765ff95e1c9bcccefacb30e8",
  "cid": "QmV1541150c08c730db4c27d5406977506c71774d025",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286045,
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
      "evaluated_at": 1760286045
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
  "sig": "0d320f307b8c9dcf955e33e471b5d6855c5a3c96f85b7c618bfcb27a56ee3410"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105151005829
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285765, 'matching_hash': 'ea26f24e3d1967f5'}}}