```json
{
  "id": "27e57d0c02da1ed9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292368,
  "host_pid": "9e6742732c60:1",
  "hash": "55762ac8931b183e52e18d731775661cd8bb1dbfdccc6a59f0fff86c4493fdd5",
  "cid": "QmV155762ac8931b183e52e18d731775661cd8bb1dbf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292368,
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
      "evaluated_at": 1760292368
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
  "sig": "87f7a1939a0b242168a347c56bfbdf5181e33d7d68285b3b74d069de2a33ee86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240979962
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 69701716, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '0560549e1456bff1'}}}