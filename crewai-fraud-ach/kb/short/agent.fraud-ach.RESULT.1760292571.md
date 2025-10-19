```json
{
  "id": "df2ea98986487408",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292571,
  "host_pid": "9e6742732c60:1",
  "hash": "59d5e233d2b42bcda2372b42544ab4ce03ca76119c6442a06b8551afc7455871",
  "cid": "QmV159d5e233d2b42bcda2372b42544ab4ce03ca7611",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292571,
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
      "evaluated_at": 1760292571
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
  "sig": "455eb92157c2872fc8a872765aad7fd46bf49e6948e3831a0afdd5c0bb6a628e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 65653200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}