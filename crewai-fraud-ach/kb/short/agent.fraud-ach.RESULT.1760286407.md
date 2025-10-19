```json
{
  "id": "2b4dcbd2228dd494",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286407,
  "host_pid": "9e6742732c60:1",
  "hash": "406f486dab62cf116ef5caed833d9d79642b3b9a7c3b643722fe525b1ce6d530",
  "cid": "QmV1406f486dab62cf116ef5caed833d9d79642b3b9a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286407,
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
      "evaluated_at": 1760286407
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
  "sig": "178c2cd72c82e601f755bb374466509264e9df741a0c878ea76514f1afd1d837"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105150676701
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11298288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285765, 'matching_hash': 'f947c72340b5e951'}}}