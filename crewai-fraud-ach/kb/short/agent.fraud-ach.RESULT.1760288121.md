```json
{
  "id": "cfde4bfc1bbbb2ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288121,
  "host_pid": "9e6742732c60:1",
  "hash": "d75cd5ec2a54d4ce0eec8bee3bbc8281c42370318e8052be4d776e631421025d",
  "cid": "QmV1d75cd5ec2a54d4ce0eec8bee3bbc8281c4237031",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288121,
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
      "evaluated_at": 1760288121
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
  "sig": "ade9431cb085b3b2bb0c668576039f970cfd1c49cea50581c6bcd7e6c15e4e2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460501611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 14077713, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285764, 'matching_hash': 'a26573d157351ea4'}}}