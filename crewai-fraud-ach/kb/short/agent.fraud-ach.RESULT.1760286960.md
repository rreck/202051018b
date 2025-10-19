```json
{
  "id": "8829f716e7fb0335",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286960,
  "host_pid": "9e6742732c60:1",
  "hash": "8fb481a0b56306814d216e54caafc1ba268e9adac5b132850ec90cb48983d2a4",
  "cid": "QmV18fb481a0b56306814d216e54caafc1ba268e9ada",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286960,
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
      "evaluated_at": 1760286960
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
  "sig": "04b56d56e0b72741787045e4ac3d5dc6e4cacf6c86349714a76a49e7b7eb5bc5"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 121000247715779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 43000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285763, 'matching_hash': 'e635467487b35661'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}