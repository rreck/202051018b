```json
{
  "id": "2b41702327652f08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288494,
  "host_pid": "9e6742732c60:1",
  "hash": "3dfbc6ac90dae423d95778f5a11220e042380eb1bb0e84e4592c908114f96bc6",
  "cid": "QmV13dfbc6ac90dae423d95778f5a11220e042380eb1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288494,
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
      "evaluated_at": 1760288494
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
  "sig": "8a9d3333b1d0d1e25ef30a9bdf2330a3b2582a17e73295c1bc817a0c73ff936f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157192911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 25501705, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285764, 'matching_hash': 'e4f1eedb707bab1f'}}}