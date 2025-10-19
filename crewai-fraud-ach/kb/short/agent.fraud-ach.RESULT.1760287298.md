```json
{
  "id": "21422507406156dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287298,
  "host_pid": "9e6742732c60:1",
  "hash": "66c78a60709241414e798ac995193ac9cd952a0052041973ec3da1b9ce349527",
  "cid": "QmV166c78a60709241414e798ac995193ac9cd952a00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287298,
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
      "evaluated_at": 1760287298
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
  "sig": "f3a0995623aa771a01519efd7b9fcff3d3e300fd97e681f8406c62683f0f0f62"
}
```

Fraud detected: duplicate_transaction (score: 72)
Transaction: 044000037578651
Details: {'velocity': {'fraud_detected': True, 'risk_score': 60, 'details': {'transaction_count': 55, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285763, 'matching_hash': '25cb229761d99325'}}}