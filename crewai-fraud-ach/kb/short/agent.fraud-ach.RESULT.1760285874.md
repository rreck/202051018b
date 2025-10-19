```json
{
  "id": "6e72f200533517c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285874,
  "host_pid": "9e6742732c60:1",
  "hash": "24031f8205f7becab32474d00358c1823c0e7f9164191edd2f62eb21a4a38fb7",
  "cid": "QmV124031f8205f7becab32474d00358c1823c0e7f91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285874,
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
      "evaluated_at": 1760285874
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
  "sig": "e28fb3444370441c935e54a22a48f39da2206f5f80f4630632b45285d4d1efaf"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009597421131
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285765, 'matching_hash': 'ee859bd02c19b1f0'}}}