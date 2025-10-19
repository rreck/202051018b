```json
{
  "id": "b8817ff33bcc67c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292412,
  "host_pid": "9e6742732c60:1",
  "hash": "ed8f72ba68cb05eab0df75bd185b14e679d2cc297fe354de548c930231090a30",
  "cid": "QmV1ed8f72ba68cb05eab0df75bd185b14e679d2cc29",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292412,
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
      "evaluated_at": 1760292412
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
  "sig": "9935145e5893b0f725306d8292cc05757bc61816eb51d0236d8cd0bccd34696d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273957576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 89201994, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': '30cc5398d3c09035'}}}