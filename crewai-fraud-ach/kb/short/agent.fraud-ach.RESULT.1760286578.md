```json
{
  "id": "844907ab04a6995c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286578,
  "host_pid": "9e6742732c60:1",
  "hash": "d5985e4090308a66586bea3b013402cc82f3e6183acd3ffb0d1e57fa3f3bc990",
  "cid": "QmV1d5985e4090308a66586bea3b013402cc82f3e618",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286578,
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
      "evaluated_at": 1760286578
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
  "sig": "3fed2e5f7bb96bb2d042d91f4a08fd5e88cc2ac601c5a6bf43f9ef9cc0a8d051"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000241053391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12854490, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285763, 'matching_hash': '6e04470f15e4fc18'}}}