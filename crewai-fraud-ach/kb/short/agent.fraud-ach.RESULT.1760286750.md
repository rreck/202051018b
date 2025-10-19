```json
{
  "id": "55f7368a9c13a274",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286750,
  "host_pid": "9e6742732c60:1",
  "hash": "c3fc73eb0d3f0bdff930ebac8ac1c0117391bc7b30b5e64007f8cacc93a03bd6",
  "cid": "QmV1c3fc73eb0d3f0bdff930ebac8ac1c0117391bc7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286750,
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
      "evaluated_at": 1760286750
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "c1330e196c6391f4802e16a0671e1c5edefdfde79790919cb80a489f2e7727ed"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105158436711
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16593300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285763, 'matching_hash': '839de208acaae015'}}}