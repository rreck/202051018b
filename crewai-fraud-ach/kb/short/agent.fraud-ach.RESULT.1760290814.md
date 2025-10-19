```json
{
  "id": "5dacbec64102f37c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290814,
  "host_pid": "9e6742732c60:1",
  "hash": "091cd33012730c08ed4e64496252f835e493edf6c5f9b033b41848007779fbd4",
  "cid": "QmV1091cd33012730c08ed4e64496252f835e493edf6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290814,
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
      "evaluated_at": 1760290814
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
  "sig": "4b7d25352b010bd74e6ffba3cb5b51f6512c03afc383a144365c38a5c61be41c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249225817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 37687840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': 'b4dc0a1cb279f16e'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}