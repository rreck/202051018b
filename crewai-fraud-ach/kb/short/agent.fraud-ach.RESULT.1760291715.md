```json
{
  "id": "8432a4fe0e1c3b71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291715,
  "host_pid": "9e6742732c60:1",
  "hash": "2729a16a46a3d1ad8498be35ed006e72fac50cf20afa40269b586eaa03233c30",
  "cid": "QmV12729a16a46a3d1ad8498be35ed006e72fac50cf2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291715,
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
      "evaluated_at": 1760291715
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
  "sig": "083222664379ecef7dc47429805467f07301a99741c5a1dee8eade394fc7c153"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279614717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 71693557, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285765, 'matching_hash': '2481e4baa9b260b7'}}}