```json
{
  "id": "58ef82a0dfb6521e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289261,
  "host_pid": "9e6742732c60:1",
  "hash": "dea23a34bf5f58111a644fef29b80a7a3b08431c74e6e3c1812e098473603385",
  "cid": "QmV1dea23a34bf5f58111a644fef29b80a7a3b08431c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289261,
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
      "evaluated_at": 1760289261
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "d88f1848d248ba3c2b935677402db9258b95cab7aea39944e725bc2e749ba6ed"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 122105159813222
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 59000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285764, 'matching_hash': 'b185e366ced12ee8'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}