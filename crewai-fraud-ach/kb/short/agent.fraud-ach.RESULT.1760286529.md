```json
{
  "id": "f9d9797a85d7b560",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286529,
  "host_pid": "9e6742732c60:1",
  "hash": "153a10ed792732d81b764c06213c02508975cd4b35263b21ca8dd8b1a068ee7a",
  "cid": "QmV1153a10ed792732d81b764c06213c02508975cd4b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286529,
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
      "evaluated_at": 1760286529
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "d60a45a57dca33995085f53cb271e00f724daf6d97be264a2e720b3975410336"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105153371756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11690840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285764, 'matching_hash': 'f6b71775dc53ea2e'}}}