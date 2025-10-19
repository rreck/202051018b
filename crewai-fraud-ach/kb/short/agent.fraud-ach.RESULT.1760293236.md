```json
{
  "id": "a2fa072aff52662a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293236,
  "host_pid": "9e6742732c60:1",
  "hash": "43a50bc9f51f7eb38481f451a3692bac810b502d9511f8ab87803fde3ab0232a",
  "cid": "QmV143a50bc9f51f7eb38481f451a3692bac810b502d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293236,
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
      "evaluated_at": 1760293236
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
  "sig": "60a3c8174d7a9e874053b015dfabe1ce10ecbd80b9da2d77b443084e15d65e6a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469927048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 63755522, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '982ed2d64f96a5b2'}}}