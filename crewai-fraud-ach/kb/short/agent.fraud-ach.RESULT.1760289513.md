```json
{
  "id": "b82dc19c10293b28",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289513,
  "host_pid": "9e6742732c60:1",
  "hash": "0f743ec3b141a58b498fde6c301b7603c65a2b68962a851b0f71bf8237961f5c",
  "cid": "QmV10f743ec3b141a58b498fde6c301b7603c65a2b68",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289513,
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
      "evaluated_at": 1760289513
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
  "sig": "683b03234cb8efd1ff92c34819bfdf8c64bb4ef933b86f3e61d90ed3fffee4b7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 26694125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285764, 'matching_hash': 'bf601f225a65579b'}}}