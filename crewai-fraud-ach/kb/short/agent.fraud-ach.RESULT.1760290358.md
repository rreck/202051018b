```json
{
  "id": "6ead7a9c2fa1ffb8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290358,
  "host_pid": "9e6742732c60:1",
  "hash": "a391ea0e3e4f9464971cbf27ec1cfd68833c62923ccac385542fa6f4bbd36e10",
  "cid": "QmV1a391ea0e3e4f9464971cbf27ec1cfd68833c6292",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290358,
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
      "evaluated_at": 1760290358
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
  "sig": "dad32b386b7fb7dfdfa202d96a7ab17ab7a77efeadc159b98e9be63273e093b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027165618
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 38686164, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}