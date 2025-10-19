```json
{
  "id": "93f619705b141c9d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288724,
  "host_pid": "9e6742732c60:1",
  "hash": "d0ce63cf8b9219d800ae3f9eb90b5b680a92e1a080fb64fba861a9f64fa88d3c",
  "cid": "QmV1d0ce63cf8b9219d800ae3f9eb90b5b680a92e1a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288724,
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
      "evaluated_at": 1760288724
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
  "sig": "4a5801456ae946338698e2e69701a2b880c36e7cb905d8eb998281c2d8baaccf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032539256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 50393100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': '34ea678ce834982a'}}}