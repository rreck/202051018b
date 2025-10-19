```json
{
  "id": "9a2430f8a5ec9504",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294400,
  "host_pid": "9e6742732c60:1",
  "hash": "806d36e10ae2f2e38f0f4cc25cb8dd903a9843be90c1b3b86d10a57a7296982e",
  "cid": "QmV1806d36e10ae2f2e38f0f4cc25cb8dd903a9843be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294400,
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
      "evaluated_at": 1760294400
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
  "sig": "95f652402031ca37a2a2766344d0b45bfec38ff9c5016b885828453c6fe6952a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461002751
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 79664232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'a9820f16c3d139ec'}}}