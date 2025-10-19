```json
{
  "id": "050cf345bc034de5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292189,
  "host_pid": "9e6742732c60:1",
  "hash": "8628b6fd44df1aff3973402baa10d929200b3245ae8e01660c64fe4a4a5f3450",
  "cid": "QmV18628b6fd44df1aff3973402baa10d929200b3245",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292189,
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
      "evaluated_at": 1760292189
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "1df73cba7d6d2ae6038e45a6d88c088c272286cb6cf82abc77c00f28137f784c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 291093508895399
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 91182336, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': 'b750a26a60b25ace'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}