```json
{
  "id": "6af4d4ddb7332cb2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289443,
  "host_pid": "9e6742732c60:1",
  "hash": "e46b1378891eff196592a1f17d4d74d9ab827475da7aa9a9c33e2b5d4dd8a5ea",
  "cid": "QmV1e46b1378891eff196592a1f17d4d74d9ab827475",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289443,
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
      "evaluated_at": 1760289443
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
  "sig": "f8f400d1149295bf29829fee56b0f4509452ae24b53bed57d8818e38c2618d78"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025325708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 39637119, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285765, 'matching_hash': '23dd43a9dda0a05d'}}}