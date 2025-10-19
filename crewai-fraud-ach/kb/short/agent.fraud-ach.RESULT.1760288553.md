```json
{
  "id": "62a947240bea6f88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288553,
  "host_pid": "9e6742732c60:1",
  "hash": "aa4a99201fefe541dff14cb6b3a14c35381074f25921df90b7689dbb51df590d",
  "cid": "QmV1aa4a99201fefe541dff14cb6b3a14c35381074f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288553,
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
      "evaluated_at": 1760288553
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
  "sig": "2ae73cd6071122f8d4062669ec4ee963c6daa67569a72c18f56d0142a4c93f91"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598639172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': '9f277109cf79f7ea'}}}een': 1760285763, 'matching_hash': 'b8896a43cee69b83'}}}