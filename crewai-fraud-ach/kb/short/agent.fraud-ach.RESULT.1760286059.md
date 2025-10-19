```json
{
  "id": "0fe50324a42722ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286059,
  "host_pid": "9e6742732c60:1",
  "hash": "66dff7c49775c3a983d5333ec044ad8a0750cd88d0b349836275fe9506a3330b",
  "cid": "QmV166dff7c49775c3a983d5333ec044ad8a0750cd88",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286059,
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
      "evaluated_at": 1760286059
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
  "sig": "eaaad40448561fc4636991530e3e600ab8c804b5ee40826382b37832eb29e671"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241053391
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285763, 'matching_hash': '6e04470f15e4fc18'}}}