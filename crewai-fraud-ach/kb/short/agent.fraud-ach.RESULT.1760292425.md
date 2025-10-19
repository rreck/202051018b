```json
{
  "id": "fd3f30b6a53985d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292425,
  "host_pid": "9e6742732c60:1",
  "hash": "1a1cefc06595e0e23f8da94398f334d368cbd492881cd10ace69e101660f933f",
  "cid": "QmV11a1cefc06595e0e23f8da94398f334d368cbd492",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292425,
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
      "evaluated_at": 1760292425
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
  "sig": "74f7a0c521ecb76fc32915d654dd668e3db7f4a5dfe5aa1c3e5d3b0d570d6dca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277678125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 63278764, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': 'e82f6ac77d9f2ce9'}}}