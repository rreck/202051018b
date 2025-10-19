```json
{
  "id": "9e397909cc6939e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288033,
  "host_pid": "9e6742732c60:1",
  "hash": "10fa33e033c7eedcc8eb87a22ee496e65417ec8aef76c1a4a914bc473cb487ad",
  "cid": "QmV110fa33e033c7eedcc8eb87a22ee496e65417ec8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288033,
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
      "evaluated_at": 1760288033
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
  "sig": "c7a3258ee48e44cbc0843ee9c038fc0722579854dab7489df34b565599d9989b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152525323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 29443520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285765, 'matching_hash': '867ad08c0d495d7b'}}}