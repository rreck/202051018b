```json
{
  "id": "fb35577ae5554722",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290541,
  "host_pid": "9e6742732c60:1",
  "hash": "3521102362671128c73e64af3f32bf83445301f898d8521b2b5da95c499bde9b",
  "cid": "QmV13521102362671128c73e64af3f32bf83445301f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290541,
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
      "evaluated_at": 1760290541
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
  "sig": "81fdcafd26c7edf3bcc9b40891b86734397f7a79141e56a71bad6a6e5c5d23cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033750281
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 60431634, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285764, 'matching_hash': '57e27cf175445fc0'}}}