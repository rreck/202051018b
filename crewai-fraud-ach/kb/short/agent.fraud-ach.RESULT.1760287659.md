```json
{
  "id": "98caa02270640271",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287659,
  "host_pid": "9e6742732c60:1",
  "hash": "0e3484ddc8000b1b1fd6590f2cdcb96ce4944dd412bbf83c9d88a983057f8a7a",
  "cid": "QmV10e3484ddc8000b1b1fd6590f2cdcb96ce4944dd4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287659,
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
      "evaluated_at": 1760287659
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
  "sig": "f2209841ff892f52987ce1e858f71edd88a1b64e158f39812c0f9679a61f34a7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000022866819
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285763, 'matching_hash': '7f3c5046f4bcc1d0'}}}een': 1760285763, 'matching_hash': '75f7f0ceec197518'}}}