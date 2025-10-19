```json
{
  "id": "2bfccf7526b98983",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287487,
  "host_pid": "9e6742732c60:1",
  "hash": "3ebd7e2994cc870641b2fa92c6841bd5971540274302469ffcf772e349b8e2c9",
  "cid": "QmV13ebd7e2994cc870641b2fa92c6841bd597154027",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287487,
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
      "evaluated_at": 1760287487
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
  "sig": "6035c0ca01d65ef1645e8dba0711dee4f85bec47402fbc2b4b5cb8147837a846"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 021000022866819
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285763, 'matching_hash': '7f3c5046f4bcc1d0'}}}een': 1760285763, 'matching_hash': 'c589ba109b80fe94'}}}