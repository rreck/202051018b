```json
{
  "id": "efe58e2882f0573e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294023,
  "host_pid": "9e6742732c60:1",
  "hash": "04845b82010129d710f0a291aa41f30ed979ff7d11078c3c75d691da0b8401aa",
  "cid": "QmV104845b82010129d710f0a291aa41f30ed979ff7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294023,
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
      "evaluated_at": 1760294023
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
  "sig": "58206076b0bc833263e1ee7f4b72b1be848208b1a09c467626a89205142ad51e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024591055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 106579010, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '8a72f4eb6bbba5d7'}}}