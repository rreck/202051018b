```json
{
  "id": "453cbece6e712a69",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293198,
  "host_pid": "9e6742732c60:1",
  "hash": "7bbfadfef099d2e0f4361f123e5292683123a821a48030d9c8e6060bc779b95b",
  "cid": "QmV17bbfadfef099d2e0f4361f123e5292683123a821",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293198,
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
      "evaluated_at": 1760293198
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
  "sig": "362e8c00f0ba32e27be1ca7e1bc4661cfb5ebe9947f0ea7d5f75215c2a89cc6d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 67786824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}