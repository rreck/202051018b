```json
{
  "id": "04e311698431e19f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294591,
  "host_pid": "9e6742732c60:1",
  "hash": "3cd0b563edb4c1408e748d428932a3119ecde90af6863ad116bfa8af2e1dcc14",
  "cid": "QmV13cd0b563edb4c1408e748d428932a3119ecde90a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294591,
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
      "evaluated_at": 1760294591
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
  "sig": "1a75005fc4ef0a5e75ffa763914c059a8fe37f56e27e17ae52c294a9cafa09ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463831807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 43446275, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'ac2384e4a351cc1b'}}}