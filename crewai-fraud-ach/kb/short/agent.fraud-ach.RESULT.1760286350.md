```json
{
  "id": "d6e8614036b0f8b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286350,
  "host_pid": "9e6742732c60:1",
  "hash": "6375d2c71da413916dc6503b271b551506e0994ad5f24d55830a9eedb79f126f",
  "cid": "QmV16375d2c71da413916dc6503b271b551506e0994a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286350,
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
      "evaluated_at": 1760286350
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
  "sig": "a2e89428d2352e31a4394e8e1df722850367e162a20da5e193023feb94265a13"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}