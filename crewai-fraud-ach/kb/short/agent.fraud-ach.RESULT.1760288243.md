```json
{
  "id": "150559427536f2c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288243,
  "host_pid": "9e6742732c60:1",
  "hash": "16ecb68fe101f6353bdd59f879b330daaacedc3ec0afc65be13aca57e3bb43a7",
  "cid": "QmV116ecb68fe101f6353bdd59f879b330daaacedc3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288243,
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
      "evaluated_at": 1760288243
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
  "sig": "5dfc13992d443a15c3da50eee78bdb8bd92692b695fdd7d5f4e788df6fbdf738"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243177921
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 29986290, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285765, 'matching_hash': '2e3fb8f97f4f3efd'}}}