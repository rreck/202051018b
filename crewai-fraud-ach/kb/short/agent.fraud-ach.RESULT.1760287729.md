```json
{
  "id": "90e8f0aa3b7b88db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287729,
  "host_pid": "9e6742732c60:1",
  "hash": "80f0d421daf72930f09d02ec11e3dd52a26bf94fee92ae90d8a9be53d288bf02",
  "cid": "QmV180f0d421daf72930f09d02ec11e3dd52a26bf94f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287729,
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
      "evaluated_at": 1760287729
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
  "sig": "d4d46a253a1040cf69401770800794e2185137c659f7035fddbffceb0dba92e4"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 026009596862432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 14283920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285764, 'matching_hash': 'ec6d2f2d96a1a77c'}}}