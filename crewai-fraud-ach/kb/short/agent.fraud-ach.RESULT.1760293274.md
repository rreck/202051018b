```json
{
  "id": "ec3734d2ebd595f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293274,
  "host_pid": "9e6742732c60:1",
  "hash": "7299de16b6e74af0f6eb8f27ddfbfabcf07629e0ac73de3876024b6d5d6bed21",
  "cid": "QmV17299de16b6e74af0f6eb8f27ddfbfabcf07629e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293274,
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
      "evaluated_at": 1760293274
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
  "sig": "03f653d2e21732e7a1d8d67319e99eaf0f5bc6d2e9db6bed55dfd8f0e4efc764"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023944450
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 16356125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '3c29e184ba733f5e'}}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '443655354', 'validation_error': 'Invalid routing number checksum'}}}