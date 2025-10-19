```json
{
  "id": "ac0fdd52ad94c541",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286003,
  "host_pid": "9e6742732c60:1",
  "hash": "341cbd2f0f8e0ef9a475c03e4620207f4498650e6d1667c550dea08e5aac5e60",
  "cid": "QmV1341cbd2f0f8e0ef9a475c03e4620207f4498650e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286003,
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
      "evaluated_at": 1760286003
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
  "sig": "f09d57d35c8aac4ae85d16920242416cb9e6f8f31e9e8aceadc8536f8535c047"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030256978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 33021198, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760284979, 'matching_hash': 'a2caca18f22a9a3d'}}}