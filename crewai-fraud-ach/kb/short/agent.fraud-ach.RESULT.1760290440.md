```json
{
  "id": "49095792ffe0c299",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290440,
  "host_pid": "9e6742732c60:1",
  "hash": "21b8225fac6114327120ed6bd08346aa2675abf7a59ccd4a5580660c63692a82",
  "cid": "QmV121b8225fac6114327120ed6bd08346aa2675abf7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290440,
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
      "evaluated_at": 1760290440
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
  "sig": "d134a4f217526cecc9240315fe24ce7ebcea7ab1c057e6954d455fcf9eed96bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 55946850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}