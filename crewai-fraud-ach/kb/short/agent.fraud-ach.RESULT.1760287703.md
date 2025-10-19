```json
{
  "id": "d4e4340c1a4dcefd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287703,
  "host_pid": "9e6742732c60:1",
  "hash": "b93736327171cd750f9253216341d95c9df93cf3447ac6a4063d978d8b9e8770",
  "cid": "QmV1b93736327171cd750f9253216341d95c9df93cf3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287703,
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
      "evaluated_at": 1760287703
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
  "sig": "0e13098709d5b2bba50edf1ae50cba737f4c26695ea604434b4fdb275ea5922d"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 122105153543170
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285765, 'matching_hash': 'bc1f881c41cfe07c'}}}