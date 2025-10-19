```json
{
  "id": "d2c6e32956777d8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293313,
  "host_pid": "9e6742732c60:1",
  "hash": "61d916068f47e2af8eb1b5d1502b14192a332406d80fb738cb7bfd77d474ab6f",
  "cid": "QmV161d916068f47e2af8eb1b5d1502b14192a332406",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293313,
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
      "evaluated_at": 1760293313
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
  "sig": "b4e24394ebcb14f340ba35f56ff13dd4e2fd6bbc5f50bc23252de4cf76b3416e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026691588
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 87408072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '1da0382cf03ec7d2'}}}}