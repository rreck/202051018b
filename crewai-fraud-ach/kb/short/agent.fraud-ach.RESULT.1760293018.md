```json
{
  "id": "be0a3ab0b305e08d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293018,
  "host_pid": "9e6742732c60:1",
  "hash": "87ee14ad7f9537592fe7c02d2028c386cbc1fd225ad9146fe7190ce1679829af",
  "cid": "QmV187ee14ad7f9537592fe7c02d2028c386cbc1fd22",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293018,
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
      "evaluated_at": 1760293018
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
  "sig": "a46f956dfbdf22caeb2dd23dfef0439a48a5947c4e4ec1284cd5f6556cf0fcde"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029518652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 15970500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': 'e772ab4f6c2a0903'}}}