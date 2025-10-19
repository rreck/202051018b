```json
{
  "id": "6d98cf42011f8390",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294469,
  "host_pid": "9e6742732c60:1",
  "hash": "afe1ff510562ea19ac033491965969280b011e316dd634706d88bbebcc7f524e",
  "cid": "QmV1afe1ff510562ea19ac033491965969280b011e31",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294469,
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
      "evaluated_at": 1760294469
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
  "sig": "1dbe6a36c2f04245c534015b779701c9002d530f89424e16306b1755e6cf0105"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035927231
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 110411294, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': '0aeb814485d84e75'}}}