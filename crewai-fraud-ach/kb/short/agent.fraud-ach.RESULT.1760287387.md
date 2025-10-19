```json
{
  "id": "6435b381e2b948cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287387,
  "host_pid": "9e6742732c60:1",
  "hash": "d467e7e9604ba68f46cd8b3a94a3a81e1df278eb4a5400acb83d5fd4f12b92ad",
  "cid": "QmV1d467e7e9604ba68f46cd8b3a94a3a81e1df278eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287387,
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
      "evaluated_at": 1760287387
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
  "sig": "2020a567a5c1b9145fa8d96f219b72765b95f6a556e19d67e17afa98ef59c834"
}
```

Fraud detected: duplicate_transaction (score: 75)
Transaction: 111000026908362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 66, 'details': {'transaction_count': 58, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285765, 'matching_hash': '7a1f70b5e24e62dd'}}}