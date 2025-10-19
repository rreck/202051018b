```json
{
  "id": "7f08dbc7c13a1f13",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294021,
  "host_pid": "9e6742732c60:1",
  "hash": "61d220af70a406d75bf4bc41a307aab838d9a19357212d2ede3643d96cd9cd30",
  "cid": "QmV161d220af70a406d75bf4bc41a307aab838d9a193",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294021,
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
      "evaluated_at": 1760294021
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
  "sig": "2f3b4c9be2a68f488307a0b2359a18f70fd5796f5696cd335aa26769b8512093"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150369382
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 82295840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '1d04175be49b6deb'}}}