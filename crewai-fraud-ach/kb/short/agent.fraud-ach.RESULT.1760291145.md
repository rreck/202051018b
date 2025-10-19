```json
{
  "id": "c477a837e9954c57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291145,
  "host_pid": "9e6742732c60:1",
  "hash": "2075d4dd53e43350bef0bff77386ecaf83079d1472e0e27427a6433afbc0defe",
  "cid": "QmV12075d4dd53e43350bef0bff77386ecaf83079d14",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291145,
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
      "evaluated_at": 1760291145
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
  "sig": "89cec4b106a2382c05c6f6f1b4f6f1832b2bdc60a7a08ddf9fc171c06b2d8ae4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468482875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 21172536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285764, 'matching_hash': '502f46d9d0122688'}}}