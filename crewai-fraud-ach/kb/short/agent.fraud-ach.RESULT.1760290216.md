```json
{
  "id": "54cab35a9b922464",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290216,
  "host_pid": "9e6742732c60:1",
  "hash": "89668c8ce4af15cd7bbfb7c77598e4cbf0317e7ccfc7bce96fc304b1ab7b92bd",
  "cid": "QmV189668c8ce4af15cd7bbfb7c77598e4cbf0317e7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290216,
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
      "evaluated_at": 1760290216
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
  "sig": "0ffdbbfac17ee10ba4335d69c10ed81d9399b77604f0bb790b78af249d919394"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 45827712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}