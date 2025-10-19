```json
{
  "id": "566be1e33e150b50",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292590,
  "host_pid": "9e6742732c60:1",
  "hash": "d60a7675da1968aeb4f8c05247f60ad5586432c71d256b237483eb8e69dd1b6c",
  "cid": "QmV1d60a7675da1968aeb4f8c05247f60ad5586432c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292590,
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
      "evaluated_at": 1760292590
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
  "sig": "1f0ae6b59b26eae386a2efe61f94d4725097d42f32d4809e99af7d69c81d77c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464768410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 94076442, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '182aec6491bb83ab'}}}