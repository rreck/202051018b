```json
{
  "id": "80aac2d3afeada7e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288720,
  "host_pid": "9e6742732c60:1",
  "hash": "b6f8ab380c716f6fa492ba1b4fc4dce0808541a7fe26dcb67a8ec018ef07dfe3",
  "cid": "QmV1b6f8ab380c716f6fa492ba1b4fc4dce0808541a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288720,
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
      "evaluated_at": 1760288720
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
  "sig": "937d96b2ed5bc529e1ef4daba8c9bdd5ff64b07fe7e02933c532b720f478244d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465236749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 24669414, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285764, 'matching_hash': '3442ebeb280b968f'}}}