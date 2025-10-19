```json
{
  "id": "ce1f66e95040b61e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294182,
  "host_pid": "9e6742732c60:1",
  "hash": "78c20c2e214fea78509695cd683652bd7eeb1d6a5f07e2ed48910eec8034c6cb",
  "cid": "QmV178c20c2e214fea78509695cd683652bd7eeb1d6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294182,
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
      "evaluated_at": 1760294183
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
  "sig": "bbc1f750967dc0944a35d24e60974581f82255f9733a5aec192654a34bf459a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465124688
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 38340849, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': 'c4099eb9aeb13a11'}}}