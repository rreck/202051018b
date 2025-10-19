```json
{
  "id": "4b5f7e9b0a0fd18b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288783,
  "host_pid": "9e6742732c60:1",
  "hash": "387f88a0ce068b27f23f4b4abf1a566f1f01d3baef466a40ff77e6c176256b83",
  "cid": "QmV1387f88a0ce068b27f23f4b4abf1a566f1f01d3ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288783,
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
      "evaluated_at": 1760288783
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "56b8a7a72de5da46a8338ce4516febebb45ff8ef8057d4888facebbcb2f53cb8"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000241606573
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 52000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285763, 'matching_hash': '2fa99cb8a6f007e0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}