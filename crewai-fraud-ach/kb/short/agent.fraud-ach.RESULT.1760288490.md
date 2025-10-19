```json
{
  "id": "a851b5570c71b877",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288490,
  "host_pid": "9e6742732c60:1",
  "hash": "634be751e4e5f799521b4f2079d60d0451f9798ec0a95789268c2dcca77b4b3f",
  "cid": "QmV1634be751e4e5f799521b4f2079d60d0451f9798e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288490,
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
      "evaluated_at": 1760288490
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
  "sig": "9c4b3cf264fc9463146adfbf9c9dda51117f41c6ea2027ecacc24e908e9664a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029122182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285763, 'matching_hash': '6eeeaf20a2fbd10d'}}}