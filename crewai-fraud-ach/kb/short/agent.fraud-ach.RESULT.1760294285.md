```json
{
  "id": "89ba0a9360c4a7fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294285,
  "host_pid": "9e6742732c60:1",
  "hash": "d52df9af0176d2458a194dbf41e13fcab2a3c90c0188ad30c7817fb3f266678f",
  "cid": "QmV1d52df9af0176d2458a194dbf41e13fcab2a3c90c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294285,
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
      "evaluated_at": 1760294285
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
  "sig": "d22a7717ec9532ffde286ce6ad3487a7e36a91beb31b1f9990ac0b471a226d88"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156493582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 30205490, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '28d5522bb9de7370'}}}