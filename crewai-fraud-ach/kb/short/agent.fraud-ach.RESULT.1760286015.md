```json
{
  "id": "1956271eacaf08fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286015,
  "host_pid": "9e6742732c60:1",
  "hash": "8c4bd23b41fec63ab1183b71a6c6716ada14b6fe28c6be33205e1dae805eb83b",
  "cid": "QmV18c4bd23b41fec63ab1183b71a6c6716ada14b6fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286015,
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
      "evaluated_at": 1760286015
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
  "sig": "1d2f4e26766ac719a7057a07f5c3615801074cfae4ce486467d31520f6247ebf"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000021480535
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285765, 'matching_hash': '9682be52dcbb3d1d'}}}