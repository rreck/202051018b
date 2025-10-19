```json
{
  "id": "e3d391e7995da1d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290159,
  "host_pid": "9e6742732c60:1",
  "hash": "59b9244cb5e69b873cb3c3bfeee058157923ec6501eb6d74b121c39dee70ff5d",
  "cid": "QmV159b9244cb5e69b873cb3c3bfeee058157923ec65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290159,
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
      "evaluated_at": 1760290159
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
  "sig": "e1e663dbb367b73b5e480407d835eb4f1b0dee10de26ad4615c8de7db9f1bf46"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026701294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 36844379, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285764, 'matching_hash': 'c6488d75609f0f90'}}}