```json
{
  "id": "e77445521fca009d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288178,
  "host_pid": "9e6742732c60:1",
  "hash": "ada9647ade9857d2dcad3233500cc389a7e761b4c7d72cefeef36b66939a2942",
  "cid": "QmV1ada9647ade9857d2dcad3233500cc389a7e761b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288178,
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
      "evaluated_at": 1760288178
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
  "sig": "8e963ee7e6b08359e63db948e36061f862119053bce2c068da630f6a6bca9809"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 42513338, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}