```json
{
  "id": "e36eec30e944683e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286723,
  "host_pid": "9e6742732c60:1",
  "hash": "b01f58634389da78eb69cf424ba41b0e02c837964833d25bca639ca3d15332b0",
  "cid": "QmV1b01f58634389da78eb69cf424ba41b0e02c83796",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286723,
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
      "evaluated_at": 1760286723
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
  "sig": "03e0bb4e8460cf937b0a32a60c8edebfb1fd9131a0430d76ac076ee2986fa07b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000025853793
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285763, 'matching_hash': 'ff3a3f7dec7a702a'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285763, 'matching_hash': '726e20d3efcb42e0'}}}