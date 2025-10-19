```json
{
  "id": "711cb89165460015",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294460,
  "host_pid": "9e6742732c60:1",
  "hash": "b4df7575e996f1c45f702b24d8e949f9d19f9388464f35159ef8261ab432f29d",
  "cid": "QmV1b4df7575e996f1c45f702b24d8e949f9d19f9388",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294460,
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
      "evaluated_at": 1760294460
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
  "sig": "f2e02e0ff4e26907b8a62ac913ef64eaf8a5af291502d5817995c76a080344ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277311413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 12362910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '8eaabbab3b444a6b'}}}