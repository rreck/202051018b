```json
{
  "id": "828209505a69b10a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286619,
  "host_pid": "9e6742732c60:1",
  "hash": "db07b9ad950ee52577602103923fe894b2270a575c8cb15e1fb853ecc62909d2",
  "cid": "QmV1db07b9ad950ee52577602103923fe894b2270a57",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286619,
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
      "evaluated_at": 1760286619
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
  "sig": "4f7511cfefeffac0223b8c1e553d2d05cc47ee6837cacac7619962f371d11bc5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467961793
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285765, 'matching_hash': '7ef856857e97207f'}}}