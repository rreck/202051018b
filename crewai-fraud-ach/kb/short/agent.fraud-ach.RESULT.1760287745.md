```json
{
  "id": "feca17926c30a2d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287745,
  "host_pid": "9e6742732c60:1",
  "hash": "505a661aaf78d568de342d668a16bf59fa414379361ec2c5e1c05bf8fcc8b863",
  "cid": "QmV1505a661aaf78d568de342d668a16bf59fa414379",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287745,
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
      "evaluated_at": 1760287745
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
  "sig": "adc2d52dfc29b9965b7ff23ae275a992b38aec5dbb9d3d30afb66cecca0a8023"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 063100272156319
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285763, 'matching_hash': '6d26908715188c7a'}}}een': 1760285763, 'matching_hash': '0723803785cdf871'}}}routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}