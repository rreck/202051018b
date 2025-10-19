```json
{
  "id": "e27963a5e4eb1f30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288125,
  "host_pid": "9e6742732c60:1",
  "hash": "45034b5d7c078dce58f9829534f754a5f097fef45e2e017a0b7f94ded8028281",
  "cid": "QmV145034b5d7c078dce58f9829534f754a5f097fef4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288125,
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
      "evaluated_at": 1760288125
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
  "sig": "2d63959bba1fe3a90071e7713ae30411197ce43d125163ae6178db97d60ec2d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247383202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 33055165, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285765, 'matching_hash': '32929947211460fd'}}}