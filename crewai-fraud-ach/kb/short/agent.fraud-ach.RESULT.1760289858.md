```json
{
  "id": "3694206a675b748d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289858,
  "host_pid": "9e6742732c60:1",
  "hash": "cf58fbe012f891c8de22102b8632516deab6f0c08c1f3abb33b0f08d7ebc11a5",
  "cid": "QmV1cf58fbe012f891c8de22102b8632516deab6f0c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289858,
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
      "evaluated_at": 1760289858
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
  "sig": "3f86ebbb8daebf906058cd1f365dd496f39c1852b10417c65894191c7000b8d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462917660
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 46666800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': '3c31ab634de6a3e3'}}}