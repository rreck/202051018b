```json
{
  "id": "8c5e3f8a4abee505",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294225,
  "host_pid": "9e6742732c60:1",
  "hash": "ebfbaec12d3b67162305351e2965a1a2cca5f4ca9e9b60de34dfcc18ae92a99c",
  "cid": "QmV1ebfbaec12d3b67162305351e2965a1a2cca5f4ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294225,
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
      "evaluated_at": 1760294225
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
  "sig": "27965b3a216cf8865f2b119e1fbb65faed6b01ec834611039c0ae9ad483ae0e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021151885
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 57302154, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285764, 'matching_hash': '925ef0ca9f93e495'}}}