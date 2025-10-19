```json
{
  "id": "a91f0488b01c47db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288916,
  "host_pid": "9e6742732c60:1",
  "hash": "3044ea195bbc67f41f423e6ce61839685d80bd573ab274a0276ff4c809a79d68",
  "cid": "QmV13044ea195bbc67f41f423e6ce61839685d80bd57",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288916,
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
      "evaluated_at": 1760288916
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
  "sig": "4920b75847a4500b0b29066320aaad2a482d771a9c6b2424f3e3aa809a226225"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022915367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 44902620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': '4fdfaefd2437a484'}}}