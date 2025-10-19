```json
{
  "id": "31849da498955895",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291028,
  "host_pid": "9e6742732c60:1",
  "hash": "58d1e5529d1aa1fa9216356491e88edfbe86de72115052b20ad08f1b25ee9d82",
  "cid": "QmV158d1e5529d1aa1fa9216356491e88edfbe86de72",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291028,
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
      "evaluated_at": 1760291028
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
  "sig": "59c69420e331e27ade0130d8b49246df2fc3e96431845fa460f10d47953284a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242027891
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 23026575, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285764, 'matching_hash': '176f574fbb51fea2'}}}