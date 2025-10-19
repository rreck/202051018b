```json
{
  "id": "0d82175440faed17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289661,
  "host_pid": "9e6742732c60:1",
  "hash": "8dba5b5bba3e13ecded971cfbf65f3f38c130094de36e2e466c2370fb38f9695",
  "cid": "QmV18dba5b5bba3e13ecded971cfbf65f3f38c130094",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289661,
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
      "evaluated_at": 1760289661
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
  "sig": "e760bf40562372997268fb8f5e45e06b25156fafffab92ebae396c73796d411a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241355402
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 21015777, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}