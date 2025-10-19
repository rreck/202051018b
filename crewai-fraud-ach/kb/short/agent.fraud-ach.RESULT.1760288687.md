```json
{
  "id": "29f0bef584f1961a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288687,
  "host_pid": "9e6742732c60:1",
  "hash": "82d44ba596e719fe07170c7288e5c72e7391b373ea57bcb6a37c81f52fa392f3",
  "cid": "QmV182d44ba596e719fe07170c7288e5c72e7391b373",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288687,
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
      "evaluated_at": 1760288687
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "05917c18647302444c64dbec5af530505a8d16de44f997ab8166723900c44051"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 060557484693193
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 43269713, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': 'db8aeeee2135ece1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '060557489', 'validation_error': 'Invalid routing number checksum'}}}