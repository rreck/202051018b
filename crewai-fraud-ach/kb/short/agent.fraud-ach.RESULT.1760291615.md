```json
{
  "id": "966dcd0612064630",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291615,
  "host_pid": "9e6742732c60:1",
  "hash": "4828396508d860deb41f5f48d1359877ac1260fb1c9aeb8bf6c5b84eefa86ba8",
  "cid": "QmV14828396508d860deb41f5f48d1359877ac1260fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291615,
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
      "evaluated_at": 1760291615
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
  "sig": "e91fe9c781243084199b16d521e003d32d9ed7f35ecc7fda1c20200519181d56"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028239803
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 48251598, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'c92648ab22001236'}}}