```json
{
  "id": "b19094666afc64b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290931,
  "host_pid": "9e6742732c60:1",
  "hash": "f8997ee5bc8d96c7f0297a0ba12aaf1daff7f3c3eac9de14c2ff0e80897b9824",
  "cid": "QmV1f8997ee5bc8d96c7f0297a0ba12aaf1daff7f3c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290931,
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
      "evaluated_at": 1760290931
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
  "sig": "cd0128fd63c53452eb5e9641fffc6e18ee13d905f01f297439b10576c5b5debd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034886670
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 22302475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'cbf6d0e6528ee173'}}}