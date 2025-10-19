```json
{
  "id": "66912f0fdacc409f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287224,
  "host_pid": "9e6742732c60:1",
  "hash": "a12193ccc86b2e36b8b95bf1f48058b22cdc909bce113d7bcd4316d9fdeb3f3e",
  "cid": "QmV1a12193ccc86b2e36b8b95bf1f48058b22cdc909b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287224,
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
      "evaluated_at": 1760287224
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
  "sig": "73f03ab203492e47dbbef89f2eef88c6042750e073a9bcc568596aae160d9713"
}
```

Fraud detected: duplicate_transaction (score: 69)
Transaction: 021000029386599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 54, 'details': {'transaction_count': 52, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}