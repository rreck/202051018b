```json
{
  "id": "98e6cd47772e68cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290713,
  "host_pid": "9e6742732c60:1",
  "hash": "d2e826e8e7f17c407c06c2150d554c3bc7c040879f25b80e6d2aac0e38aedf24",
  "cid": "QmV1d2e826e8e7f17c407c06c2150d554c3bc7c04087",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290713,
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
      "evaluated_at": 1760290713
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
  "sig": "b395676bf1c5d873b81823d9b0b3ee04894ab4a09df91f6761777df0f9923e77"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 53334156, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}