```json
{
  "id": "7dc8500e3697bcf1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292341,
  "host_pid": "9e6742732c60:1",
  "hash": "fc33863c9562060102beb7d7e25f549a56bd21a3f0e11f9ac90501aea2cd6784",
  "cid": "QmV1fc33863c9562060102beb7d7e25f549a56bd21a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292341,
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
      "evaluated_at": 1760292341
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
  "sig": "8a51640211991217beeaef161a04b87b25c9fa17cab20b517c2ef5a128b7677f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 64011870, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}