```json
{
  "id": "04364fbdb551b6bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288602,
  "host_pid": "9e6742732c60:1",
  "hash": "036d7249fcfff9e057ddf4f8602a185b9145cbe71623d3349d1239f53cee2d25",
  "cid": "QmV1036d7249fcfff9e057ddf4f8602a185b9145cbe7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288602,
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
      "evaluated_at": 1760288602
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
  "sig": "aec435100d0b193ccbc6f0f30bd22d1e23c6f1c290660d792326f3c80e48d083"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279614717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 38817506, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285765, 'matching_hash': '2481e4baa9b260b7'}}}