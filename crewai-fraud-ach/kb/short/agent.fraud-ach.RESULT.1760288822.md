```json
{
  "id": "e1bda86cba219fac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288822,
  "host_pid": "9e6742732c60:1",
  "hash": "b34ecc0c5d1dff7f1cf2f6a6e85d3f3b015aedada180e465dedcc5c82bc99765",
  "cid": "QmV1b34ecc0c5d1dff7f1cf2f6a6e85d3f3b015aedad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288822,
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
      "evaluated_at": 1760288822
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
  "sig": "8ab6886204024aeb42b6602528aa3734dca5feb2c0220a68be558780a9b4c5ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034056272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 14513310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285763, 'matching_hash': 'aae4e2a94575911d'}}}