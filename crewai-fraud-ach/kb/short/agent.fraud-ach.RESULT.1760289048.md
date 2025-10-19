```json
{
  "id": "9728e3bf722350f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289048,
  "host_pid": "9e6742732c60:1",
  "hash": "5b5afa2490927aa9321c53b414d174320a1d499269785cabd78ad1e4075baeb6",
  "cid": "QmV15b5afa2490927aa9321c53b414d174320a1d4992",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289048,
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
      "evaluated_at": 1760289048
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
  "sig": "0d97c3b011c7ec2da2ef0a700e8cc5ff99ecc1791bb1735e586dd2de9b7634b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275563549
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 47598320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': 'a33681b350a57503'}}}