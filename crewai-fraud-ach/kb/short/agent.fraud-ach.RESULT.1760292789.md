```json
{
  "id": "af6e735fdfb38407",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292789,
  "host_pid": "9e6742732c60:1",
  "hash": "a26ca20ef59edb0e3802e7438d597617afd06f25a542c0d438d7c3355a044d37",
  "cid": "QmV1a26ca20ef59edb0e3802e7438d597617afd06f25",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292789,
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
      "evaluated_at": 1760292789
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
  "sig": "ff3e2bcbdf6ff3d4324d1787ced604fe5a7719cb08ce1a5e81a52d13c9ee257f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030478037
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 44210300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': 'a92b61c306bd8c34'}}}