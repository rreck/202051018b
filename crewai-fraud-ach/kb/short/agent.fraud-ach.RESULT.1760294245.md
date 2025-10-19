```json
{
  "id": "b6146faa298bec34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294245,
  "host_pid": "9e6742732c60:1",
  "hash": "60abfc6daf8eb885749efd0730173a492968a2c0a3b146ba8dde52bdad9aea5c",
  "cid": "QmV160abfc6daf8eb885749efd0730173a492968a2c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294245,
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
      "evaluated_at": 1760294245
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
  "sig": "342b67be61d7c206ba526a5fedb2ffd3fa8253032d9ff4fa55f2cc1965a3608a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021748494
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 13422942, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': '2adbcd1f80c0d3e0'}}}