```json
{
  "id": "b21a962e5c20b9b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294340,
  "host_pid": "9e6742732c60:1",
  "hash": "d7b169980bb3aebcd2ab39b748d0b46dcdbeb820f0dc2134bfa4487ae8a1832d",
  "cid": "QmV1d7b169980bb3aebcd2ab39b748d0b46dcdbeb820",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294340,
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
      "evaluated_at": 1760294340
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
  "sig": "42f17886cd26ce1c3300f21e63d9e46f031c68e30f6e9277415e400a8b43e00b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028475138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 78446400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'fd3dd6a8db70ef91'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}