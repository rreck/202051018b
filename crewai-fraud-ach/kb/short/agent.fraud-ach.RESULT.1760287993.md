```json
{
  "id": "e0fbff64c8572262",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287993,
  "host_pid": "9e6742732c60:1",
  "hash": "ffbf3a6d72ff7dd934bf1d001996a38d0ca8643708fa753e3ea264647cc59909",
  "cid": "QmV1ffbf3a6d72ff7dd934bf1d001996a38d0ca86437",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287993,
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
      "evaluated_at": 1760287993
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
  "sig": "cfea4eda12febefbd236c4b0e8338d7a67330315206cf723a76f2ba6561ae8e7"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201460873764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 39500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285763, 'matching_hash': '6dda2db9e90937c1'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}