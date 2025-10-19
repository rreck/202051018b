```json
{
  "id": "8fccd14491273eb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287997,
  "host_pid": "9e6742732c60:1",
  "hash": "1bb4f074c1920e2b0c4c68a138aa177ffd07499698b49cdfa4c3474dd48ef166",
  "cid": "QmV11bb4f074c1920e2b0c4c68a138aa177ffd074996",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287997,
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
      "evaluated_at": 1760287997
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
  "sig": "fe88b7da3bfde1d9c123617fefd6ee702808c837982388cf65093ba1e63e780a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020141329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 37323550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285764, 'matching_hash': '1e11ace6091d7a38'}}}