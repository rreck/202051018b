```json
{
  "id": "230a5be871716817",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293235,
  "host_pid": "9e6742732c60:1",
  "hash": "99746d8df86e00717ab4437feab8b8247d2f6ed11b3cdcb6a479eca62851f2ea",
  "cid": "QmV199746d8df86e00717ab4437feab8b8247d2f6ed1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293235,
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
      "evaluated_at": 1760293235
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
  "sig": "3bd94c7805fe4f8d01f38e89073a59c539d5a4508d33f308f21f4bd9c61e9bab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244797937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 84740148, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285765, 'matching_hash': 'e00995c9aab9b89d'}}}