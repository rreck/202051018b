```json
{
  "id": "a4dc85c90f687e40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292513,
  "host_pid": "9e6742732c60:1",
  "hash": "e614a127460bc1718ef66da8bd1ff7bec317435772e218cabc0146cfd2053d4b",
  "cid": "QmV1e614a127460bc1718ef66da8bd1ff7bec3174357",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292513,
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
      "evaluated_at": 1760292513
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
  "sig": "ce5dd8c986abe7d5ff49ff65e5cb0a5b882c697b622e0487651db5907154b5fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152187504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 94016356, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285764, 'matching_hash': '4c6bc703d31ba532'}}}}