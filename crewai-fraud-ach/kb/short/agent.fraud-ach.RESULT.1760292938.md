```json
{
  "id": "d1ed6fc9d18fc04e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292938,
  "host_pid": "9e6742732c60:1",
  "hash": "89c1e2fad111a78f6172560153fae3399d9188a24b5565be355444055d7a907e",
  "cid": "QmV189c1e2fad111a78f6172560153fae3399d9188a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292938,
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
      "evaluated_at": 1760292938
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
  "sig": "d04a0ea1e21c5d743684a4ce516f916e136d99d760c5315e25d18f4b972dd01f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151773289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 102307296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': '7b1e6accdb666d6e'}}}