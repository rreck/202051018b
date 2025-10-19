```json
{
  "id": "69b57dd4aa520b96",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292086,
  "host_pid": "9e6742732c60:1",
  "hash": "9000309192d4a0d398129f04ab3eb23e914b3d89a5db4ad406815b1a3a31e730",
  "cid": "QmV19000309192d4a0d398129f04ab3eb23e914b3d89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292086,
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
      "evaluated_at": 1760292086
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
  "sig": "274199e8ad394317e8464e242be0ba94fe2fbf323e740f5f4c78debed2189b04"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022025451
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 89004550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': '147c6cadc877e9f2'}}}