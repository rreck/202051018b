```json
{
  "id": "69b1bd4293af10f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291434,
  "host_pid": "9e6742732c60:1",
  "hash": "0a0836e4ed4721cdd6ad6ec2c00dab0ac882f2282e6dcd0c9c4907d0836931c3",
  "cid": "QmV10a0836e4ed4721cdd6ad6ec2c00dab0ac882f228",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291434,
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
      "evaluated_at": 1760291434
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
  "sig": "8354cfaaec44a3df6c25e1a211e5bfc62aafbec161d237f31f9962ec01b530f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591362528
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 74808125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '85f76e3ae9d0eff6'}}}