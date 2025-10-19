```json
{
  "id": "73c551ca5ec7e656",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293290,
  "host_pid": "9e6742732c60:1",
  "hash": "f6c97729af0bdc3342e75454872e33e339751e118c7b6aedc80911906d152121",
  "cid": "QmV1f6c97729af0bdc3342e75454872e33e339751e11",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293290,
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
      "evaluated_at": 1760293290
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
  "sig": "068cb9bec0f418117cba51f1632ba6dadeb1b778ee2cefec7e4591bd6ca79095"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465632833
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 103605060, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285765, 'matching_hash': '908d3acbf69a371c'}}}