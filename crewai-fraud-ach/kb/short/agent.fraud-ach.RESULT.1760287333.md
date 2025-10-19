```json
{
  "id": "bf49731cb14291ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287333,
  "host_pid": "9e6742732c60:1",
  "hash": "199c178ace49d90f57f60117194107f9ef90e78125ec1d4e6dd6a3f8d23078e6",
  "cid": "QmV1199c178ace49d90f57f60117194107f9ef90e781",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287333,
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
      "evaluated_at": 1760287333
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
  "sig": "721adefe9e550453c3f9ee4c82de53eeb42982883c1823d3db0d68cd0eedc2a3"
}
```

Fraud detected: duplicate_transaction (score: 73)
Transaction: 121000242521033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 62, 'details': {'transaction_count': 56, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}