```json
{
  "id": "bcb61541db6cf020",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294200,
  "host_pid": "9e6742732c60:1",
  "hash": "cf27a77bb27bebbca283af7aaf8a3e47f834155e740a13dbf7ff1be708a8e4fe",
  "cid": "QmV1cf27a77bb27bebbca283af7aaf8a3e47f834155e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294200,
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
      "evaluated_at": 1760294200
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
  "sig": "18a1113a0f60c920291931863f8bfb5913ba097628117d5d168f5ecdcc2bf94d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597164999
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 41755930, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': 'b2fd55917469a01e'}}}