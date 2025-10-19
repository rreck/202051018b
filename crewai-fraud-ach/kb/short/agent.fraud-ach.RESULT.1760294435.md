```json
{
  "id": "e8338576307db9c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294435,
  "host_pid": "9e6742732c60:1",
  "hash": "2d6eaa8d4ae91613da3d94ca88918809d2e0a061a5154cc02c09d1b7fe0b4391",
  "cid": "QmV12d6eaa8d4ae91613da3d94ca88918809d2e0a061",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294435,
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
      "evaluated_at": 1760294435
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
  "sig": "9366492396304df78939b60ce3546dbe61e7ac071c5cec95c69e1fe09cab0db1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027679172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 103353404, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'bcf2a51730a73925'}}}