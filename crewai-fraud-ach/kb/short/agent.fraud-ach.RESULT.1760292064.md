```json
{
  "id": "7c0a9b9cf74376a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292064,
  "host_pid": "9e6742732c60:1",
  "hash": "75ad184cbdd94859c665b773f14eb71b74b551734ec6493769d37421babccfbd",
  "cid": "QmV175ad184cbdd94859c665b773f14eb71b74b55173",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292064,
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
      "evaluated_at": 1760292064
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
  "sig": "ff6de266c110d6860f76ceec2bac14253f616ccbd70a99e13c6db797fff7861c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242987850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 22118481, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285764, 'matching_hash': 'ac2312cc15fe4af9'}}}