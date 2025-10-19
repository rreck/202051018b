```json
{
  "id": "0a60dcb2a8366e54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294345,
  "host_pid": "9e6742732c60:1",
  "hash": "3dfd1adcdd5ae63b14fa9184f910185ae29c93e0838fa437837c4a9b79ffe01a",
  "cid": "QmV13dfd1adcdd5ae63b14fa9184f910185ae29c93e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294345,
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
      "evaluated_at": 1760294345
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
  "sig": "5e504a1e491f3a850a3786e76d1347d91f0ba9ae7193d5272d7a56e88a989dac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279804164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 55679952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '5884f0f9ee4a893d'}}}