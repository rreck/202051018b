```json
{
  "id": "26530f070c3f8129",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290289,
  "host_pid": "9e6742732c60:1",
  "hash": "6481dd677ae4cf5cee6f81455ee5e8400ea5c54a82f304d26fe704499385b86e",
  "cid": "QmV16481dd677ae4cf5cee6f81455ee5e8400ea5c54a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290289,
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
      "evaluated_at": 1760290289
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
  "sig": "1cb62e84fcc0465a86cc2c16b99ab89a9e910d4b557b9776ce265b76d0aefe31"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 40386082, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285765, 'matching_hash': 'a63e704272eccc25'}}}