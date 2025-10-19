```json
{
  "id": "37a9222c55616133",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294618,
  "host_pid": "9e6742732c60:1",
  "hash": "22e2e5f7bfcc21ab4fe3677b3d9ccd38643a6e047cfe972f3bbabdd754520ec2",
  "cid": "QmV122e2e5f7bfcc21ab4fe3677b3d9ccd38643a6e04",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294618,
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
      "evaluated_at": 1760294618
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
  "sig": "a9f2fd16ff468990d03b3f3817738bacd3a9d4719e3b06063d964f03c69f414f"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463431091
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 120500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'c719f059714014d6'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}