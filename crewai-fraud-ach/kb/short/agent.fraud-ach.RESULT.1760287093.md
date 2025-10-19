```json
{
  "id": "0489435bc503e5d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287093,
  "host_pid": "9e6742732c60:1",
  "hash": "cd5b007176a19c508249dde7cc9bc0bb52d112622d679f912ebfb0bcaa099914",
  "cid": "QmV1cd5b007176a19c508249dde7cc9bc0bb52d11262",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287093,
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
      "evaluated_at": 1760287093
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "fdaaf78c4b4c737a50ad155fef0b0027e5d7358ca7e1159711cb4270ca488639"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009592351032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10121328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285763, 'matching_hash': '5f413645b746a025'}}}