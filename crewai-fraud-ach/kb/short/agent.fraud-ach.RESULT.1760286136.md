```json
{
  "id": "c27d5a773b24d954",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286136,
  "host_pid": "9e6742732c60:1",
  "hash": "81c87796cb9edb49d05e23a40f1f7022eef994e160be32ffb33502831d809f29",
  "cid": "QmV181c87796cb9edb49d05e23a40f1f7022eef994e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286136,
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
      "evaluated_at": 1760286136
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
  "sig": "2b0ba86e66c094f5202da79c1522c4528486ef9126dfd402c26ee8b6e36dad53"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241355402
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}