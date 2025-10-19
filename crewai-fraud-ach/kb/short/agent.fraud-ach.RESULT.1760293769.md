```json
{
  "id": "c64b238cba07dcb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293769,
  "host_pid": "9e6742732c60:1",
  "hash": "846d2214811e7fe6c38ade1fe95504bfbb1226e9dba022b5b063736adb82e4bf",
  "cid": "QmV1846d2214811e7fe6c38ade1fe95504bfbb1226e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293769,
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
      "evaluated_at": 1760293769
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
  "sig": "47398ec49a357366af8977116f3be5ab746a91b3fd12b1fe36f2119d4ac131b5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 13299525, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}