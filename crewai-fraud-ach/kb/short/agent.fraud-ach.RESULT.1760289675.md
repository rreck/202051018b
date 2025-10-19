```json
{
  "id": "860bb342b1ea3158",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289675,
  "host_pid": "9e6742732c60:1",
  "hash": "11f9bb38f134a8668816ee3fa9ee4898eadb62cce6f4d842413936031e4d14b9",
  "cid": "QmV111f9bb38f134a8668816ee3fa9ee4898eadb62cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289675,
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
      "evaluated_at": 1760289675
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
  "sig": "be4de9459f2deee193c618318c21ac2654977e47c86f909e8a31c3384024c8cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038495907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 35360260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': '3a0df0e30691ba23'}}}