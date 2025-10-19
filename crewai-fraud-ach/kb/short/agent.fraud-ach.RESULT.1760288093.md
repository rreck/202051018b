```json
{
  "id": "6e35e4ad1eb053fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288093,
  "host_pid": "9e6742732c60:1",
  "hash": "ec1b2e0e300ae9ab8b20c51c3327ceb429ebc5ab81a7cfee1d33acc20c507bd9",
  "cid": "QmV1ec1b2e0e300ae9ab8b20c51c3327ceb429ebc5ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288093,
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
      "evaluated_at": 1760288093
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
  "sig": "e66cfd1933241f2829d5af51a5a55bc7d61232ea090f5999cc3f4a210e8859a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248581748
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 15677334, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285765, 'matching_hash': '6ba0c7e0a23e9d51'}}}