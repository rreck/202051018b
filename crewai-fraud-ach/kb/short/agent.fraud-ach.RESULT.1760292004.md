```json
{
  "id": "d835c7cd30f36083",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292004,
  "host_pid": "9e6742732c60:1",
  "hash": "ae43682a299dc5bb3515d2ae4bc501a8f6805e320192658781121bbc11ac3089",
  "cid": "QmV1ae43682a299dc5bb3515d2ae4bc501a8f6805e32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292004,
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
      "evaluated_at": 1760292004
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
  "sig": "fb68c1f1d9267630a99b55f1e942e4464ef0a003f6ee557fb975930f8a1c8305"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244807015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 18800000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285764, 'matching_hash': 'e3fbbc71f2accf8f'}}}