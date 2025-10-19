```json
{
  "id": "b4b9df0a3b0b5139",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289360,
  "host_pid": "9e6742732c60:1",
  "hash": "a6e44b307f7a312ce93408f08f8bc48a3d14695a57e4c434f9d7cff17afee408",
  "cid": "QmV1a6e44b307f7a312ce93408f08f8bc48a3d14695a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289360,
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
      "evaluated_at": 1760289360
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
  "sig": "b0d42127126cbfec6161c810c5e1b0b261567366471772b5c36707469a6b2c03"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240263900
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 30250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285764, 'matching_hash': 'e5d68d31887f65d4'}}}