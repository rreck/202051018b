```json
{
  "id": "5eaff1f85d88881d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290824,
  "host_pid": "9e6742732c60:1",
  "hash": "26e3dbc1065f4df214c8bbcf9e38733b8aee1ddc8353af1eeb923903c136140e",
  "cid": "QmV126e3dbc1065f4df214c8bbcf9e38733b8aee1ddc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290824,
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
      "evaluated_at": 1760290824
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
  "sig": "59f6b575ee5f15670237fecb9919ba25fec974ce0d0ce76e853ecf3a6268a23d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026281875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 65554880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': 'ee0b29e0b2882e41'}}}