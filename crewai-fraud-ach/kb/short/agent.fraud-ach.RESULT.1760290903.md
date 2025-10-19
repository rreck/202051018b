```json
{
  "id": "8ae0e6351ebd2a3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290903,
  "host_pid": "9e6742732c60:1",
  "hash": "aac0666cf8045a312c9171776fa6645686a12b4d8400c954b619076c528d61f4",
  "cid": "QmV1aac0666cf8045a312c9171776fa6645686a12b4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290903,
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
      "evaluated_at": 1760290903
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
  "sig": "5843088ede3d609f63dfe85d5dcbcfc7b7a02b13f17257ed8d108fe27e81797c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039536800
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 28946484, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': '37ca22243c3304cf'}}}