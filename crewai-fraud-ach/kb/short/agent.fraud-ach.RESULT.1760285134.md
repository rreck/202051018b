```json
{
  "id": "982760bd883b96d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285134,
  "host_pid": "9e6742732c60:1",
  "hash": "47394c50fe92e173103970fbb53c8ba009f668cfc4d69ad82ace0ec267b98708",
  "cid": "QmV147394c50fe92e173103970fbb53c8ba009f668cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285134,
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
      "evaluated_at": 1760285134
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
  "sig": "cf088e3b28627943247ce2d618d5b8a4c11d7dafeee52de80e287a1581c3e62d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}