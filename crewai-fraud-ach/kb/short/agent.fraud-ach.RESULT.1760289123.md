```json
{
  "id": "f68e0b40ad7d2997",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289123,
  "host_pid": "9e6742732c60:1",
  "hash": "60685b388ae590c3299447c0e48666b472f5760d37aa2247ec65f43a8d9ede06",
  "cid": "QmV160685b388ae590c3299447c0e48666b472f5760d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289123,
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
      "evaluated_at": 1760289123
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
  "sig": "cfc6a5d282e2029889a7945e4825ceddf3120b22e0baaca388222c07be35ae42"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593769639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 48934272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': 'cb8c3421a3879068'}}}