```json
{
  "id": "5743557f82fb01ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293664,
  "host_pid": "9e6742732c60:1",
  "hash": "c388e011d99257c55e1a45790ba71d3dd3e254872598b08fc095465227195aad",
  "cid": "QmV1c388e011d99257c55e1a45790ba71d3dd3e25487",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293664,
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
      "evaluated_at": 1760293664
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
  "sig": "e73eed9723d6c7fec0bd043fadb8b1c834c35d7ca6d78b0cb702fe62db8809b3"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 122105152842303
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 111500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285764, 'matching_hash': 'f130ef58b190a1ab'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}