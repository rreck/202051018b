```json
{
  "id": "cc88bf1e032de782",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288326,
  "host_pid": "9e6742732c60:1",
  "hash": "da4d43f38b103b2a2a0497ecd180bb0e7396cbbe402ae401b1fa202f45eadc23",
  "cid": "QmV1da4d43f38b103b2a2a0497ecd180bb0e7396cbbe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288326,
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
      "evaluated_at": 1760288326
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
  "sig": "557cad7bfa3779b12d32be603c3fdf2a116ea8c0cb4c3c3e12db517253a2d42c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242021792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 38799360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285763, 'matching_hash': '6b62929422267286'}}}