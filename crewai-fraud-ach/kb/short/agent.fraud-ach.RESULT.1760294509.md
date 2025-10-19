```json
{
  "id": "08b1091af55fad57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294509,
  "host_pid": "9e6742732c60:1",
  "hash": "50cd9e72512667ea802061d535bd34b3cbb70abfaf04509a2b2c1bcf9a8ec2cc",
  "cid": "QmV150cd9e72512667ea802061d535bd34b3cbb70abf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294509,
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
      "evaluated_at": 1760294509
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
  "sig": "0514812a161aec91a2a18b94641592cac8d372869d94daba1a28a79a9122a5cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245772760
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 15819410, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}}