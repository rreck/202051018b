```json
{
  "id": "9233ca933631d6c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294829,
  "host_pid": "9e6742732c60:1",
  "hash": "b3a59b9ab5f294639f870573921ad0cd32948c475a00f9c6c1677a8bd49f7a2f",
  "cid": "QmV1b3a59b9ab5f294639f870573921ad0cd32948c47",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294829,
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
      "evaluated_at": 1760294829
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
  "sig": "6f80283e7a527a0babe433ad3a62a21bb9954885b1d7582564074621d362a8a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036487644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 321, 'threshold': 50, 'total_amount': 135043737, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 320, 'first_seen': 1760284979, 'matching_hash': '0d42dcc750e3a553'}}}