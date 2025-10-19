```json
{
  "id": "bc4a7f4fcde2b7b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289341,
  "host_pid": "9e6742732c60:1",
  "hash": "028e8d7631bc9e93121947044bc2a4d9fe320369d62f437924389640fe580935",
  "cid": "QmV1028e8d7631bc9e93121947044bc2a4d9fe320369",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289341,
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
      "evaluated_at": 1760289341
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
  "sig": "3ce5995d698ea00b9d84c074238ff3d3675afee9327a0f6bb7497a3a98008e54"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241265060
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 54762120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285765, 'matching_hash': '7bee400a4c5e15b1'}}}