```json
{
  "id": "295572403df0c46f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290016,
  "host_pid": "9e6742732c60:1",
  "hash": "0623925747e4690b1d9263ce21a5db957ebe52e68361adc37c8904f4216e8b5d",
  "cid": "QmV10623925747e4690b1d9263ce21a5db957ebe52e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290016,
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
      "evaluated_at": 1760290016
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
  "sig": "bf9ce6604b37ae0cc51468fc93ec00e46c96215357ff6dc4662aa78ce4b377fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241821144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 68181724, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': '9191e5c904ced497'}}}