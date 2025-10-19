```json
{
  "id": "8ce3651ea492d382",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286576,
  "host_pid": "9e6742732c60:1",
  "hash": "fd112ae26fc0b415cb6d3711eb8e4c7bbf87e395b867581d3be004c9028f773c",
  "cid": "QmV1fd112ae26fc0b415cb6d3711eb8e4c7bbf87e395",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286576,
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
      "evaluated_at": 1760286576
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
  "sig": "7dc5ccae729dde84b523e2c9af07330a1ac91772bc797426a4b3f8eccb29c34d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105158436711
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13827750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285763, 'matching_hash': '839de208acaae015'}}}