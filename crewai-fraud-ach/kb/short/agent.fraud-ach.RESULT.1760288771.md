```json
{
  "id": "958532c4eb51e0b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288771,
  "host_pid": "9e6742732c60:1",
  "hash": "32c4287b3ff18d5f755eb39a34972f688c8701131057a8ae664de4a4e1d4775c",
  "cid": "QmV132c4287b3ff18d5f755eb39a34972f688c870113",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288771,
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
      "evaluated_at": 1760288771
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
  "sig": "2bd2dd6afcf7e71883a3e4dfe970ce45a2a57d994ed8feba4154397511f48485"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 32779544, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}