```json
{
  "id": "07c633dd449eb7af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289014,
  "host_pid": "9e6742732c60:1",
  "hash": "61013db33d2757801d912def726d07fceeab3147771717c8863857928a6aadb5",
  "cid": "QmV161013db33d2757801d912def726d07fceeab3147",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289014,
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
      "evaluated_at": 1760289014
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
  "sig": "08eb92eff434f21dbf4519f7bf63d586f3e17fb8576dad1211caef77b1ed13b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465006650
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 20259609, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285763, 'matching_hash': 'ac98f3afdd973e27'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}s': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018549}}}